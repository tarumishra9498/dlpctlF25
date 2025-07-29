from typing import override
import numpy as np
from ALP4 import ALP4, ALPError
from numpy._typing import NDArray
from PySide6.QtCore import QMutex, QMutexLocker, QThread


class DlpThread(QThread):
    def __init__(self) -> None:
        super().__init__()
        self.device: ALP4 = ALP4(version="4.1")
        self.connected: bool = False
        self.set_img_seq_mutex: QMutex = QMutex()
        self._img_seq: NDArray[np.int64] | None = None

    @override
    def run(self) -> None:
        if self.img_seq:
            self.device.Run(None, True)  # pyright: ignore[reportUnknownMemberType]

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
    def img_seq(self) -> NDArray[np.int64] | None:
        return self._img_seq

    @img_seq.setter
    def img_seq(self, new_img_seq: NDArray[np.int64] | None) -> None:
        """
        Push a new image sequence to the DLP
        """
        if new_img_seq is None:
            self._img_seq = None
        else:
            with QMutexLocker(self.set_img_seq_mutex):
                if self.validate_img_seq(new_img_seq):
                    # Pause and get rid of old sequence if already allocated
                    if self.img_seq:
                        self._img_seq = None
                        self.device.Halt()
                        self.device.FreeSeq()

                    # Allocate and push new sequence data
                    self.device.SeqAlloc(nbImg=1, bitDepth=new_img_seq.shape[2])
                    padded_seq = self.pad_seq_centered(new_img_seq)
                    self.device.SeqPut(padded_seq)
                    self._img_seq = padded_seq

    def pad_seq_centered(self, img_seq: NDArray) -> NDArray:
        target_x = self.device.nSizeX
        target_y = self.device.nSizeY

        actual_x = img_seq.shape[0]
        actual_y = img_seq.shape[1]

        pad_rows = (target_y - actual_y) // 2
        pad_cols = (target_x - actual_x) // 2

        return np.pad(
            array=img_seq,
            pad_width=((pad_rows, pad_rows), (pad_cols, pad_cols)),
            mode="constant",
            constant_values=0,
        )

    def validate_img_seq(self, img_seq: NDArray) -> bool:
        """
        Returns True if img_seq is a valid image sequence for the DLP to allocate/use
        """
        return img_seq.shape <= (self.device.nSizeX, self.device.nSizeY)

    def close(self) -> None:
        self.device.Halt()
        self.device.FreeSeq()
        self.device.Free()

    def stop(self) -> None:
        self.quit()

    def __del__(self) -> None:
        self.close()
