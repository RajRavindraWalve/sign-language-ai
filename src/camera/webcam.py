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

    def start(self, window_name, frame_processor=None, key_handler=None):

        while True:

            success, frame = self.cap.read()

            if not success:
                print("Failed to read camera.")
                break

            if frame_processor is not None:
                frame = frame_processor(frame)

            current_time = time.time()

            delta = current_time - self.previous_time
            fps = 1 / delta if delta > 0 else 0
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

            key = cv2.waitKey(1) & 0xFF

            if key_handler is not None:

                should_exit = key_handler(key)

                if should_exit:
                    break

        self.cap.release()
        cv2.destroyAllWindows()