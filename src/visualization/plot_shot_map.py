import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch


def plot_shot_map(
    shots,
    xg_column,
    title=None,
    save_path=None
):
    """
    Plot actual shots with marker size representing predicted xG.

    Parameters
    ----------
    shots : DataFrame
        Shot-level data containing x, y, goal, and predicted xG.

    xg_column : str
        Column containing the model's predicted xG.

    title : str, optional
        Figure title.

    save_path : str or Path, optional
        Location where the figure should be saved.
    """

    pitch = VerticalPitch(
        pitch_type="statsbomb",
        half=True,
        pitch_color="white",
        line_color="black"
    )

    fig, ax = pitch.draw(figsize=(8, 10))

    goals = shots[shots["goal"] == 1]
    non_goals = shots[shots["goal"] == 0]

    # Non-goals
    pitch.scatter(
        non_goals["x"],
        non_goals["y"],
        s=non_goals[xg_column] * 500 + 10,
        edgecolors="black",
        facecolors="none",
        linewidth=0.8,
        alpha=0.6,
        ax=ax,
        label="No Goal"
    )

    # Goals
    pitch.scatter(
        goals["x"],
        goals["y"],
        s=goals[xg_column] * 500 + 10,
        edgecolors="black",
        linewidth=0.8,
        alpha=0.9,
        ax=ax,
        label="Goal"
    )

    if title:
        ax.set_title(
            title,
            fontsize=16,
            pad=15
        )

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=2,
        frameon=False
    )

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    return fig, ax