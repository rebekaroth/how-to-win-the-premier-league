import pandas as pd


FILE = "data/processed/shots.csv"


def main():
    df = pd.read_csv(FILE)

    print("Dataset shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nGoal count:")
    print(df["goal"].value_counts())

    print("\nGoal rate:")
    print(df["goal"].mean())

    print("\nUnique values:")
    for column in ["body_part", "technique", "shot_type", "play_pattern"]:
        print(f"\n{column}:")
        print(df[column].value_counts())


if __name__ == "__main__":
    main()
