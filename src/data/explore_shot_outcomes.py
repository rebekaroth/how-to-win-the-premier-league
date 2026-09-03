import json
import glob
from collections import Counter

EVENT_FILES = "data/raw/events/*.json"


def main():
    outcomes = Counter()

    for file in glob.glob(EVENT_FILES):
        with open(file, "r") as f:
            events = json.load(f)

        for event in events:
            if event["type"]["name"] != "Shot":
                continue

            outcome = event["shot"]["outcome"]["name"]
            outcomes[outcome] += 1

    print("Shot outcomes:")
    print("-" * 30)

    total = sum(outcomes.values())

    for outcome, count in outcomes.most_common():
        percentage = 100 * count / total
        print(f"{outcome}: {count} ({percentage:.2f}%)")

    print("-" * 30)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
