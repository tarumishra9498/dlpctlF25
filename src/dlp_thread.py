from typing import TypeAlias, override
import numpy as np
from ALP4 import ALP4, ALPError
from PySide6.QtCore import QMutex, QMutexLocker, QThread

Img: TypeAlias = np.ndarray[tuple[int, int, int], np.dtype[np.integer]]


class DlpThread(QThread):
    def __init__(self) -> None:
        super().__init__()
        self.device: ALP4 = ALP4(version="4.1")
        self.running: bool = True
        self.connected: bool = False
        self.set_img_mutex: QMutex = QMutex()
        self._img: Img | None = None

    @override
    def run(self) -> None:
        if self.img is not None and not self.running:
            self.device.Run(None, True)  # pyright: ignore[reportUnknownMemberType]
        else:
            pass

    def open(self) -> bool:
        """
        Open connection to DLP
        """
        try:
            self.device.Initialize()
            self.connected = True
            return True
        except ALPError:
            self.connected = True
            return False

    @property
    def img(self) -> Img | None:
        return self._img

    @img.setter
    def img(self, new_img: Img | None) -> None:
        """
        Push a new image sequence to the DLP
        """
        if new_img is None:
            self._img = None
        else:
            with QMutexLocker(self.set_img_mutex):
                if self.validate_img(new_img):
                    # Pause and get rid of old sequence if already allocated
                    if self.img:
                        self._img = None
                        self.device.Halt()
                        self.device.FreeSeq()

                    # Allocate and push new sequence data
                    self.device.SeqAlloc(nbImg=1, bitDepth=1)
                    padded_seq = self.pad_img_centered(new_img)
                    self.device.SeqPut(padded_seq)

                    self.device.SetTiming(pictureTime=20_000)
                    self._img = padded_seq

    def pad_img_centered(self, img: Img) -> Img:
        target_x = self.device.nSizeX
        target_y = self.device.nSizeY

        actual_x = img.shape[0]
        actual_y = img.shape[1]

        pad_rows = (target_y - actual_y) // 2
        pad_cols = (target_x - actual_x) // 2

        print(f"nSizeX: {self.device.nSizeX}")
        print(f"nSizeY: {self.device.nSizeY}")
        print(f"pad_rows: {pad_rows}")
        print(f"pad_cols: {pad_cols}")

        padded_img = np.pad(
            array=img,
            pad_width=((pad_cols, pad_cols), (pad_rows, pad_rows)),
            mode="constant",
            constant_values=0,
        )
        return padded_img

    def validate_img(self, img: Img) -> bool:
        """
        Returns True if img is a valid image for the DLP to allocate/use
        """
        return img.shape <= (self.device.nSizeX, self.device.nSizeY)

    def close(self) -> None:
        self.device.Halt()
        self.device.FreeSeq()
        self.device.Free()

    def stop(self) -> None:
        self.quit()

    def __del__(self) -> None:
        self.close()
