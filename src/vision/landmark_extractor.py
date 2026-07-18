import numpy as np


class LandmarkExtractor:

    def extract(self, results):

        if not results.multi_hand_landmarks:
            return None

        hand = results.multi_hand_landmarks[0]

        landmarks = []

        for landmark in hand.landmark:

            landmarks.append([
                landmark.x,
                landmark.y,
                landmark.z
            ])

        return np.array(landmarks, dtype=np.float32)