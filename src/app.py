from camera.webcam import Webcam
from config.settings import *

from vision.hand_detector import HandDetector
from vision.landmark_extractor import LandmarkExtractor
from vision.drawing import HandDrawer

from utils.landmark_inspector import LandmarkInspector

from collector.dataset_collector import DatasetCollector
from config.labels import LABELS


class App:

    def __init__(self):

        self.detector = HandDetector()
        self.extractor = LandmarkExtractor()
        self.drawer = HandDrawer()
        self.inspector = LandmarkInspector()
        self.collector = DatasetCollector(LABELS)

        self.latest_landmarks = None

        self.camera = Webcam(
            CAMERA_INDEX,
            FRAME_WIDTH,
            FRAME_HEIGHT,
        )

    def process_frame(self, frame):

        results = self.detector.detect(frame)

        self.latest_landmarks = self.extractor.extract(results)

        frame = self.drawer.draw_landmarks(frame, results)

        return frame

    def handle_key(self, key):

        if key == ord("q"):
            return True

        if key == ord("l"):
            self.inspector.print_landmarks(
                self.latest_landmarks
            )

        if key == ord("n"):
            self.collector.next_label()

        if key == ord("p"):
            self.collector.previous_label()

        print(self.collector.current_label())
        
        return False

    def run(self):

        self.camera.start(
            WINDOW_NAME,
            self.process_frame,
            self.handle_key,
        )