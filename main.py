# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Generate the categorical plot and save it
fig_cat = draw_cat_plot()
fig_cat.savefig("catplot.png")
print("Categorical plot saved as catplot.png")

# Show the categorical plot
plt.show()

# Generate the heatmap and save it
fig_heat = draw_heat_map()
fig_heat.savefig("heatmap.png")
print("Heatmap saved as heatmap.png")

# Show the heatmap
plt.show()
