"""
Unit tests for plotting.py
"""

import matplotlib.pyplot as plt

from src.plotting import generate_plots


def test_generate_plots_returns_figure():
    """Test that generate_plots returns a matplotlib Figure."""
    fig = generate_plots()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 4  # We expect 4 subplots
