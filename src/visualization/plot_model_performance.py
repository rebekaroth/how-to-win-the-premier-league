import matplotlib.pyplot as plt


def plot_model_performance(
    results,
    metric,
    ylabel,
    title,
    save_path=None
):
    """
    Compare one evaluation metric across xG models.

    Parameters
    ----------
    results : DataFrame
        Must contain 'model' and the requested metric column.

    metric : str
        Column to plot.

    ylabel : str
        Label for the y-axis.

    title : str
        Figure title.

    save_path : str or Path, optional
        Location where the figure should be saved.
    """

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        results["model"],
        results[metric],
        marker="o"
    )

    ax.set_xlabel("Model")
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    ax.grid(
        axis="y",
        alpha=0.3
    )

    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    return fig, ax