import sys

from ALP4 import ALP4, ALPError


class DlpThread:
    def __init__(self) -> None:
        self.dmd: ALP4 = ALP4(version="4.1")
        self.connected = False

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

    def __del__(self) -> None:
        if self.dmd:
            self.dmd.Halt()
            self.dmd.Free()
