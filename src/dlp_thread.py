import time
from ctypes import c_long

import numpy as np
from ALP4 import ALP4, ALPError
from numpy._typing import NDArray
from PySide6.QtCore import QMutex, QMutexLocker, QThread


class DlpThread(QThread):
    def __init__(self) -> None:
        self.device: ALP4 = ALP4(version="4.1")
        self.connected = False
        self.img_seqs: list[NDArray] = []
        self.seq_ids: list[c_long] = []
        self.load_bitmask_mutex = QMutex()

    def run(self) -> None:
        for i, _ in enumerate(self.img_seqs):
            print(f"Running img_seq {i + 1}")
            self.device.Run(self.seq_ids[i], loop=True)

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

    def push(self, img_seq: NDArray) -> None:
        """
        Push a new image sequence to the DLP
        """
        with QMutexLocker(self.load_bitmask_mutex):
            if self.validate_img_seq(img_seq):
                self.img_seqs.append(img_seq)
                id = self.device.SeqAlloc(nbImg=1, bitDepth=img_seq.shape[2])
                self.seq_ids.append(id)

                padded_seq = self.pad_seq_centered(img_seq)
                self.device.SeqPut(padded_seq)

    def pad_seq_centered(self, img_seq: NDArray) -> NDArray:
        target_x = self.device.nSizeX
        target_y = self.device.nSizeY

        actual_x = img_seq.size[0]
        actual_y = img_seq.size[1]

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
        for id in self.seq_ids:
            self.device.FreeSeq(id)
        self.device.Free()

    def stop(self):
        self.quit()

    def __del__(self) -> None:
        self.close()
