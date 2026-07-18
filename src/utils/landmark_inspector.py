from utils.landmark_names import LANDMARK_NAMES


class LandmarkInspector:

    def print_landmarks(self, landmarks):

        if landmarks is None:
            print("\nNo hand detected.\n")
            return

        print("\n" + "=" * 60)
        print("HAND LANDMARKS")
        print("=" * 60)

        for index, landmark in enumerate(landmarks):

            print(f"\n[{index}] {LANDMARK_NAMES[index]}")

            print(f"    x : {landmark['x']:.4f}")
            print(f"    y : {landmark['y']:.4f}")
            print(f"    z : {landmark['z']:.4f}")

        print("\n" + "=" * 60)