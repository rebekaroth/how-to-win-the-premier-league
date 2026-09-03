import json
import glob
from collections import Counter


EVENT_FILES = "data/raw/events/*.json"


def main():

    shot_count = 0
    shot_keys = Counter()

    for file in glob.glob(EVENT_FILES):

        with open(file, "r") as f:
            events = json.load(f)

        for event in events:

            if event["type"]["name"] != "Shot":
                continue

            shot_count += 1

            # Record the fields contained in the shot object
            for key in event["shot"].keys():
                shot_keys[key] += 1

    print(f"Total shots: {shot_count}")
    print("\nFields in shot objects:")

    for key, count in shot_keys.most_common():
        print(f"{key}: {count}/{shot_count}")


if __name__ == "__main__":
    main()
