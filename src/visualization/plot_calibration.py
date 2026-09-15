import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


def plot_calibration(
    y_true,
    y_pred,
    model_name,
    n_bins=10,
    save_path=None
):
    """
    Plot predicted xG against observed goal frequency.
    """

    observed, predicted = calibration_curve(
        y_true,
        y_pred,
        n_bins=n_bins,
        strategy="quantile"
    )

    fig, ax = plt.subplots(figsize=(6, 6))

    # Perfect calibration
    ax.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Perfect calibration"
    )

    # Model calibration
    ax.plot(
        predicted,
        observed,
        marker="o",
        label=model_name
    )

    ax.set_xlabel("Predicted xG")
    ax.set_ylabel("Observed Goal Rate")
    ax.set_title(f"Calibration — {model_name}")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.legend()

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    return fig, ax