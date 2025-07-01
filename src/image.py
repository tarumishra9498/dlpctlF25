from ALP4 import ALP4
import numpy as np
from numpy._typing import NDArray


class ImageSeq:
    """
    This class represents a sequence of images to be fed into dlp. Every method requires passing in the target dmd device as an argument

    Attributes:
        width (int) : Width of image in pixels
        height (int): Height of image in pixels
        frame_count (int): How many frames the sequence will have
        image_data: Data of each frame concatenated into one big `NDArray`
        alloc_dmd (ALP4): The dlp this sequence is allocated to, None if not allocated
        alloc_id (ALP4_ID): The ID of the sequence in the dlp's memory
    """

    def __init__(self, width: int, height: int, frame_count: int, data=None) -> None:
        """
        Args:
            width: Width of image in pixels
            height: Height of image in pixels
            frame_count: How many frames the sequence will have
        """
        self.width = width
        self.height = height
        self.frame_count = frame_count
        if data:
            self._image_data = np.concatenate(data)
        else:
            self._image_data = None

        self.alloc_dmd = None
        self.alloc_id = None

    def __del__(self):
        self.deallocate()

    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, data: list[NDArray]):
        """
        This setter allows the user to not worry about deallocating and reallocating the image from dlp memory every time they update the image data
        """
        if self.alloc_dmd:
            dmd = self.alloc_dmd
            self.deallocate()

            self._image_data = np.concatenate(data)

            self.allocate(dmd)
        else:
            self._image_data = np.concatenate(data)

    def allocate(self, dmd: ALP4) -> None:
        """
        Allocate sequence to `dmd`'s memory and store the allocated sequence's ID
        """
        if not self.alloc_dmd:
            self.alloc_id = dmd.SeqAlloc(nbImg=self._image_data.shape[0], bitDepth=8)
            self.alloc_dmd = dmd
        print("ImageSeq allocated to dlp")

    def deallocate(self) -> None:
        """
        Remove the sequence from dlp's memory
        """
        if self.alloc_dmd:
            self.alloc_dmd.FreeSeq()
            self.alloc_dmd = None
            self.alloc_id = None
