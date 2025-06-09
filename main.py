
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

fig_cat = draw_cat_plot()
fig_cat.savefig("catplot.png")
print("Categorical plot saved as catplot.png")

plt.show()

fig_heat = draw_heat_map()
fig_heat.savefig("heatmap.png")
print("Heatmap saved as heatmap.png")

plt.show()
