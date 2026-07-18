import cv2
import time


class Webcam:

    def __init__(self, camera_index, width, height):

        self.cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Could not open camera with index {camera_index}"
            )

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.previous_time = time.time()

    def start(self, window_name):

        while True:

            success, frame = self.cap.read()

            if not success:
                print("Failed to read camera.")
                break

            current_time = time.time()

            fps = 1 / (current_time - self.previous_time)

            self.previous_time = current_time

            cv2.putText(
                frame,
                f"FPS: {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow(window_name, frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()