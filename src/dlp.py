import sys

from exception import DlpctlException

if sys.platform == "win32":
    from ALP4 import ALP4, ALPError

    class DLP:
        def __init__(self) -> None:
            self.dmd: ALP4 | None = ALP4(version="4.1")

            print("DLP found")
            try:
                self.dmd.Initialize()
            except ALPError:
                self.dmd = None
                raise DlpctlException("DLP not found")

        def __del__(self) -> None:
            if self.dmd:
                self.dmd.Halt()
                self.dmd.Free()
else:

    class MockDLP:
        """
        Class to mock a DLP object on platforms where you can't actually use the DLP library
        """

        def __init__(self) -> None:
            print(
                "Using mock dlp object due to unsupported OS/platform. No dlp functionality will actually happen"
            )
