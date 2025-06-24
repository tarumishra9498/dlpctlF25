from ALP4 import ALP4, ALPError

from exception import DlpctlException


class DLP:
    def __init__(self) -> None:
        self.dmd: ALP4 | None = ALP4(version="4.1")

        try:
            self.dmd.Initialize()
        except ALPError:
            self.dmd = None
            raise DlpctlException("DLP not found")

    def __del__(self) -> None:
        if self.dmd:
            self.dmd.Halt()
            self.dmd.Free()
