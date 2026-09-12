import pandas as pd
from sklearn.model_selection import train_test_split


def train_test_split_by_match(
    df,
    test_size=0.2,
    random_state=42
):
    """
    Split a shot dataset into training and test sets at the match level.

    All shots from a given match remain in the same split.
    """

    match_ids = df["match_id"].unique()

    train_matches, test_matches = train_test_split(
        match_ids,
        test_size=test_size,
        random_state=random_state
    )

    train = df[df["match_id"].isin(train_matches)].copy()
    test = df[df["match_id"].isin(test_matches)].copy()

    return train, test