from ALP4 import ALP4
import numpy as np

from image import ImageSeq


def rect_rotation_center(dmd: ALP4, framerate: int):
    """
    This function draws a rotating rectangle at `framerate` on the `dmd`

    Args:
        dmd: The DLP device/connection
        framerate: Framerate of animation, should not exceed 1000
    """
    # In milliseconds
    frametime = 1_000_000 / framerate

    dmd.SeqAlloc()
    dmd.SetTiming(pictureTime=frametime)

    frame_count = 358
    rect_image_seq = ImageSeq(200, 100, frame_count)

    blank_rect = np.zeros([rect_image_seq.width, rect_image_seq.height])

    rect_image_seq.image_data = [blank_rect]
    print(rect_image_seq.image_data)

    dmd.Run()
    input("Press Enter when done viewing animation")


if __name__ == "__main__":
    # Load dll
    dmd = ALP4(version="4.1")

    # Initialize connection to DMD
    dmd.Initialize()

    rect_rotation_center(dmd=dmd, framerate=1000)

    # Stop device
    dmd.Halt()

    # De-allocate device
    dmd.Free()
