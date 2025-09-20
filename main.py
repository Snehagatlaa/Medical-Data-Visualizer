# main.py
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Draw and save the categorical plot
    fig1 = draw_cat_plot()
    fig1.savefig("catplot.png")
    plt.close(fig1)

    # Draw and save the heatmap
    fig2 = draw_heat_map()
    fig2.savefig("heatmap.png")
    plt.close(fig2)

    print("Plots saved: catplot.png, heatmap.png")
