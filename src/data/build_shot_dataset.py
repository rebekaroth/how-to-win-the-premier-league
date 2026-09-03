import json
import glob
import os
import pandas as pd


EVENT_FILES = "data/raw/events/*.json"
OUTPUT_FILE = "data/processed/shots.csv"


def extract_shots():
    shots = []

    for file in glob.glob(EVENT_FILES):

        match_id = int(os.path.splitext(os.path.basename(file))[0])

        with open(file, "r") as f:
            events = json.load(f)

        for event in events:

            if event["type"]["name"] != "Shot":
                continue

            shot = event["shot"]

            shots.append({
                # Match information
                "match_id": match_id,
                "period": event["period"],
                "minute": event["minute"],
                "second": event["second"],

                # Team and player
                "team": event["team"]["name"],
                "player": event["player"]["name"],

                # Shot location
                "x": event["location"][0],
                "y": event["location"][1],

                # Outcome
                "goal": int(shot["outcome"]["name"] == "Goal"),

                # Shot characteristics
                "body_part": shot["body_part"]["name"],
                "technique": shot["technique"]["name"],
                "shot_type": shot["type"]["name"],

                # Context
                "play_pattern": event["play_pattern"]["name"],

                # Optional variables
                "first_time": shot.get("first_time"),
                "aerial_won": shot.get("aerial_won"),
                "one_on_one": shot.get("one_on_one"),
                "deflected": shot.get("deflected"),
                "open_goal": shot.get("open_goal"),
                "saved_off_target": shot.get("saved_off_target"),
                "redirect": shot.get("redirect"),
                "saved_to_post": shot.get("saved_to_post"),
                "follows_dribble": shot.get("follows_dribble"),

                # StatsBomb benchmark
                "statsbomb_xg": shot["statsbomb_xg"],
            })

    return pd.DataFrame(shots)


def main():
    print("Extracting shots...")

    df = extract_shots()

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved {len(df)} shots to {OUTPUT_FILE}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()
