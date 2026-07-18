from camera.webcam import Webcam
from config.settings import *
from vision.hand_detector import HandDetector
from vision.landmark_extractor import LandmarkExtractor
from vision.drawing import HandDrawer


def process_frame(frame):

    results = detector.detect(frame)
    landmarks = extractor.extract(results)
    frame = drawer.draw_landmarks(frame, results)
    return frame


detector = HandDetector()
extractor = LandmarkExtractor()
drawer = HandDrawer()


def main():

    camera = Webcam(
        CAMERA_INDEX,
        FRAME_WIDTH,
        FRAME_HEIGHT,
    )

    camera.start(
        WINDOW_NAME,
        process_frame,
    )


if __name__ == "__main__":
    main()