from pypylon import pylon
from pypylon.pylon import InstantCamera, RuntimeException


class Camera:
    def __init__(self) -> None:
        try:
            self.basler: InstantCamera = (
                pylon.TlFactory.GetInstance().CreateFirstDevice()
            )
            print("Using Basler Camera: ", self.basler.GetDeviceInfo().GetModelName())

            self.basler.PixelFormat.Value = "Mono8"
            self.basler.ExposureAuto.Value = "Off"
            self.basler.Gain.Value = 0

            self.max_exposure = 20000
            self.min_exposure = 100
            self.basler.ExposureTime.Value = 100

            self.basler.AcquisitionFrameRateEnable.Value = False
            self.basler.AcquisitionFrameRate.Value = 100
        except RuntimeException:
            self.camera = None
            print("No Basler Camera found")

    def start(self) -> None:
        self.basler.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def stop(self) -> None:
        self.basler.Close()

    def __del__(self) -> None:
        self.stop()
