import json
import os
import urllib.request


COMPETITION_ID = 2
SEASON_ID = 27

BASE_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"

MATCHES_FILE = "data/raw/matches/premier_league_2015_2016.json"
EVENTS_DIR = "data/raw/events"


def download_file(url, output_path):
    """Download a file if it does not already exist."""
    if os.path.exists(output_path):
        print(f"Already exists: {output_path}")
        return

    print(f"Downloading: {output_path}")
    urllib.request.urlretrieve(url, output_path)


def main():
    os.makedirs(EVENTS_DIR, exist_ok=True)

    with open(MATCHES_FILE, "r") as f:
        matches = json.load(f)

    print(f"Found {len(matches)} matches.")

    for i, match in enumerate(matches, start=1):
        match_id = match["match_id"]

        url = f"{BASE_URL}/events/{match_id}.json"
        output_path = os.path.join(EVENTS_DIR, f"{match_id}.json")

        print(f"[{i}/{len(matches)}] ", end="")
        download_file(url, output_path)


if __name__ == "__main__":
    main()
