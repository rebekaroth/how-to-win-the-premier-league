import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch


def plot_xg_surface(
    predict_xg,
    title=None,
    resolution=1,
    cmap="viridis",
    vmin=0,
    vmax=0.8,
    save_path=None
):
    """
    Plot an xG probability surface on a StatsBomb pitch.

    Parameters
    ----------
    predict_xg : callable
        Function accepting arrays of x and y coordinates and returning
        predicted xG values.

    title : str, optional
        Plot title.

    resolution : float
        Distance between grid points in StatsBomb coordinates.

    cmap : str
        Matplotlib colormap.

    vmin, vmax : float
        Shared xG scale. Keeping these constant allows models to be
        compared visually.

    save_path : str or Path, optional
        Location where the figure should be saved.
    """

    # Only model the attacking half
    x = np.arange(80, 120, resolution)
    y = np.arange(0, 80 + resolution, resolution)

    xx, yy = np.meshgrid(x, y)

    # Predict xG at every location
    xg = predict_xg(
        xx.ravel(),
        yy.ravel()
    ).reshape(xx.shape)

    # Create pitch
    pitch = Pitch(
    pitch_type="statsbomb",
    half=True,
    pitch_color="white",
    line_color="black"
)

    fig, ax = pitch.draw(figsize=(8, 6))
    ax.set_xlim(80, 120)

    # Plot probability surface
    surface = ax.pcolormesh(
        xx,
        yy,
        xg,
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        shading="auto",
        alpha=0.8
    )

    colorbar = fig.colorbar(
        surface,
        ax=ax,
        fraction=0.035,
        pad=0.02
    )

    colorbar.set_label("Expected Goals (xG)")

    if title:
        ax.set_title(
            title,
            fontsize=14,
            pad=12
        )

    if save_path:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    return fig, ax
