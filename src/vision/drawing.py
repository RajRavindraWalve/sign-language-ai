import cv2
import mediapipe as mp


class HandDrawer:

    def __init__(self):

        self.drawer = mp.solutions.drawing_utils
        self.hands = mp.solutions.hands

    def draw_landmarks(self, frame, results):

        if not results.multi_hand_landmarks:
            return frame

        for hand_landmarks in results.multi_hand_landmarks:

            self.drawer.draw_landmarks(
                frame,
                hand_landmarks,
                self.hands.HAND_CONNECTIONS
            )

        return frame