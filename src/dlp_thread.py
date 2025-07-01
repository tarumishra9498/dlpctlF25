import sys

if sys.platform == "win32":
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
                self.dmd = None
                self.connected = True
                return False

        def __del__(self) -> None:
            if self.dmd:
                self.dmd.Halt()
                self.dmd.Free()
else:

    class MockDlpThread:
        """
        Class to mock a `DlpThread` object on platforms where you can't actually use the DLP library
        """

        def __init__(self) -> None:
            self.connected = False
            print(
                "Using mock dlp class due to unsupported OS/platform. No dlp functionality will actually happen"
            )

        def open(self) -> bool:
            """
            Open connection to DLP (mock version)
            """
            self.connected = True
            return True
