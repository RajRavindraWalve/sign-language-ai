from camera.webcam import Webcam
from config.settings import *


def main():

    camera = Webcam(
        CAMERA_INDEX,
        FRAME_WIDTH,
        FRAME_HEIGHT
    )

    camera.start(WINDOW_NAME)


if __name__ == "__main__":
    main()