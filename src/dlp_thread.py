from ALP4 import ALP4, ALPError
from PySide6.QtCore import QThread


class DlpThread(QThread):
    def __init__(self) -> None:
        self.dmd: ALP4 = ALP4(version="4.1")
        self.connected = False

    def run(self) -> None:
        self.dmd.Wait()

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

    def stop(self):
        self.quit()

    def __del__(self) -> None:
        if self.dmd:
            self.dmd.Halt()
            self.dmd.Free()
