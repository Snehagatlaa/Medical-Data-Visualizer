# test_module.py
import pytest
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.figure

def test_draw_cat_plot_returns_figure():
    fig = draw_cat_plot()
    assert isinstance(fig, matplotlib.figure.Figure), "draw_cat_plot should return a matplotlib Figure"

def test_draw_heat_map_returns_figure():
    fig = draw_heat_map()
    assert isinstance(fig, matplotlib.figure.Figure), "draw_heat_map should return a matplotlib Figure"
