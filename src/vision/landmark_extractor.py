class LandmarkExtractor:

    def extract(self, results):

        if not results.multi_hand_landmarks:
            return None

        hand = results.multi_hand_landmarks[0]

        landmarks = []

        for landmark in hand.landmark:

            landmarks.append({
                "x": landmark.x,
                "y": landmark.y,
                "z": landmark.z
            })

        return landmarks