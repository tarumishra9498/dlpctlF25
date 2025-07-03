from ctypes import c_long
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
        alloc_id (c_long): The ID of the sequence in the dlp's memory
    """

    def __init__(
        self, width: int, height: int, frame_count: int, dmd: ALP4, data
    ) -> None:
        """
        Parameters:
            width: Width of image in pixels
            height: Height of image in pixels
            frame_count: How many frames the sequence will have
        """
        self.width: int = width
        self.height: int = height
        self.frame_count: int = frame_count
        self._image_data: NDArray

        self.alloc_dmd: ALP4 = dmd
        self.alloc_id: c_long | None = None

        self.image_data = data

    def __del__(self):
        self._deallocate()

    @property
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, data: list[NDArray]):
        """
        This setter allows the user to not worry about deallocating and reallocating the image from dlp memory every time they update the image data
        """
        if self.alloc_id:
            self._deallocate()

        img_black = np.zeros([self.alloc_dmd.nSizeY, self.alloc_dmd.nSizeX])
        img_white = np.ones([self.alloc_dmd.nSizeY, self.alloc_dmd.nSizeX]) * (2**8 - 1)
        self._image_data = np.concatenate([img_black.ravel(), img_white.ravel()])

        self._allocate()

    def _allocate(self) -> None:
        """
        Allocate sequence to `dmd`'s memory and store the allocated sequence's ID
        """
        print("_allocate")
        if self._image_data is not None and not self.alloc_id:
            self.alloc_id = self.alloc_dmd.SeqAlloc(
                nbImg=self._image_data.shape[0], bitDepth=1
            )
            self.alloc_dmd.SeqPut(self.image_data, self.alloc_id)
            print("ImageSeq allocated to dlp")
        else:
            print(
                f"ImageSeq already allocated to {self.alloc_dmd}, nothing will change"
            )

    def _deallocate(self) -> None:
        """
        Remove the sequence from `dmd`'s memory
        """
        print("_deallocate")
        if self.alloc_id:
            self.alloc_dmd.FreeSeq()
            self.alloc_id = None

    def run(self, loop: bool = True) -> None:
        """
        Display the sequence on `self.alloc_dmd`
        """
        if self.alloc_id:
            self.alloc_dmd.Run(self.alloc_id, loop)
        else:
            print("Sequence is not allocated to any DLP device")
