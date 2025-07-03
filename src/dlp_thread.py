import time
from ctypes import c_long

import numpy as np
from ALP4 import ALP4, ALPError
from numpy._typing import NDArray
from PySide6.QtCore import QThread


class DlpThread(QThread):
    def __init__(self) -> None:
        self.dmd: ALP4 = ALP4(version="4.1")
        self.connected = False
        self.img_seqs: list[NDArray] = []
        self.seq_ids: list[c_long] = []

    def run(self) -> None:
        for i, _ in enumerate(self.img_seqs):
            print(f"Running img_seq {i + 1}")
            self.dmd.Run(self.seq_ids[i], loop=True)
            time.sleep(10)

    def open(self) -> bool:
        """
        Open connection to DLP
        """
        try:
            self.dmd.Initialize()
            self.connected = True
            return True
        except ALPError:
            self.connected = True
            return False

    def push(self, img_seq: NDArray) -> None:
        """
        Push a new image sequence to the DLP
        """
        if self.validate_img_seq(img_seq):
            self.img_seqs.append(img_seq)
            id = self.dmd.SeqAlloc(nbImg=1, bitDepth=img_seq.shape[2])
            self.seq_ids.append(id)

            additional_bits = (self.dmd.nSizeX * self.dmd.nSizeY) - (
                img_seq.shape[0] * img_seq.shape[1]
            )
            padded_seq = np.pad(
                array=img_seq.ravel(),
                pad_width=additional_bits,
                constant_values=0,
            )
            self.dmd.SeqPut(padded_seq)

    def validate_img_seq(self, img_seq: NDArray) -> bool:
        """
        Returns True if img_seq is a valid image sequence for the DLP to allocate/use
        """
        if (
            img_seq is not None
            and img_seq.shape <= (self.dmd.nSizeX, self.dmd.nSizeY)
            and True
            and True
            and True
        ):
            return True
        else:
            return False

    def close(self) -> None:
        self.dmd.Halt()
        self.dmd.Free()

    def stop(self):
        self.quit()

    def __del__(self) -> None:
        self.close()
