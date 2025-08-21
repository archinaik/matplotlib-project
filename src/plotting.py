"""
plotting.py

Provides functions to create a 2x2 grid of line subplots using Matplotlib,
with customizable data generation using NumPy.

This module demonstrates:
- Creating multi-axes plots with titles, labels, and tick formatting.
- Aligning labels and titles for clarity.
- Clean, reusable function structure for plotting.
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_plots() -> plt.Figure:
    """
    Create a 2x2 figure with example line plots.

    Returns
    -------
    matplotlib.figure.Figure
        A Figure object containing a 2x2 grid of subplots.
    """
    figure, axes = plt.subplots(2, 2, layout="constrained")

    # Top-left subplot: simple range plot
    top_left = axes[0][0]
    x_vals = np.arange(0, 1_000_000, 1_000)
    top_left.plot(x_vals)
    top_left.set_title("Top-Left Plot")
    top_left.set_ylabel("Value")

    # Top-right subplot: descending line
    top_right = axes[0][1]
    x_desc = np.arange(1.0, 0.0, -0.1) * 2_000.0
    y_desc = np.arange(1.0, 0.0, -0.1)
    top_right.plot(x_desc, y_desc)
    top_right.set_title("Top-Right Plot")
    top_right.xaxis.tick_top()
    top_right.tick_params(axis="x", rotation=55)

    # Bottom row plots: reused descending data
    for idx, subplot in enumerate(axes[1]):
        subplot.plot(x_desc, y_desc)
        subplot.set_xlabel(f"X Label {idx}")
        subplot.set_ylabel(f"Y Label {idx}")
        if idx == 0:
            subplot.tick_params(axis="x", rotation=55)

    # Align labels and titles across the figure
    figure.align_labels()
    figure.align_titles()

    return figure


if __name__ == "__main__":
    fig = generate_plots()
    plt.show()
