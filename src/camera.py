from PySide6.QtCore import QThread
from pypylon import pylon
from pypylon.pylon import InstantCamera, RuntimeException
import cv2

from exception import DlpctlException


class Camera(QThread):
    def __init__(self, desired_fps=100) -> None:
        super().__init__()
        self.recording: bool = False
        self.out: cv2.VideoWriter | None = None

        self.desired_fps = desired_fps

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
                self.converter.OutputPixelFormat = pylon.PixelType_Mono8
                self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        except RuntimeException:
            self.basler = None
            raise DlpctlException("Basler camera not found")

    def start_grabbing(self) -> None:
        """
        Continuously grab the latest image in the background
        """
        if self.basler:
            self.basler.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def stop_grabbing(self) -> None:
        if self.basler:
            self.basler.StopGrabbing()

    def start_recording(self):
        print("recording")
        if self.basler:
            fourcc = cv2.VideoWriter.fourcc(*"mp4v")
            output_filename = "output.mp4"
            self.out = cv2.VideoWriter(
                output_filename,
                fourcc,
                30,
                (1280, 1024),
                isColor=False,
            )
        self.recording = True

    def stop_recording(self):
        self.recording = False
        if self.out:
            self.out.release()
            self.out = None

    def run(self) -> None:
        accumulator = 0
        if self.basler:
            if not self.basler.IsGrabbing():
                self.start_grabbing()
            while self.basler.IsGrabbing():
                grab_result = self.basler.RetrieveResult(
                    5000, pylon.TimeoutHandling_ThrowException
                )

                if grab_result.GrabSucceeded():
                    image = self.converter.Convert(grab_result)
                    img_array = image.GetArray()
                    if self.recording and self.out and self.out.isOpened():
                        self.out.write(img_array)

    def __del__(self) -> None:
        if self.basler:
            self.basler.Close()
