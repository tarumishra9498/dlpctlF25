from pypylon import pylon
from pypylon.pylon import InstantCamera, RuntimeException

from exception import DlpctlException


class Camera:
    def __init__(self) -> None:
        try:
            self.basler: InstantCamera | None = pylon.InstantCamera(
                pylon.TlFactory.GetInstance().CreateFirstDevice()
            )

            if self.basler:
                print(
                    "Using Basler Camera: ", self.basler.GetDeviceInfo().GetModelName()
                )
                self.basler.Open()
                self.basler.PixelFormat.Value = "Mono8"
                self.basler.ExposureAuto.Value = "Off"
                self.basler.Gain.Value = 0

                self.max_exposure = 20000
                self.min_exposure = 100
                self.basler.ExposureTime.Value = 100

                self.basler.AcquisitionFrameRateEnable.Value = False
                self.basler.AcquisitionFrameRate.Value = 100

                self.converter = pylon.ImageFormatConverter()
                self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
                self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        except RuntimeException:
            self.basler = None
            raise DlpctlException("Basler camera not found")

    def start(self) -> None:
        """
        Continuously grab the latest image in the background
        """
        if self.basler:
            self.basler.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def stop(self) -> None:
        if self.basler:
            self.basler.StopGrabbing()

    def run(self) -> None:
        if self.basler:
            if self.basler.IsGrabbing():
                grab_result = self.basler.RetrieveResult(
                    5000, pylon.TimeoutHandling_ThrowException
                )

                if grab_result.GrabSucceeded():
                    image = self.converter.Convert(grab_result)
                    img_array = image.GetArray()
                    print(img_array)

                grab_result.Release()

    def __del__(self) -> None:
        if self.basler:
            self.basler.Close()
