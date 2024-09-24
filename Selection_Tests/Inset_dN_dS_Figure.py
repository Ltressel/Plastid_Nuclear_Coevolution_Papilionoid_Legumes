import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set the directory where the CSV file is located and the output will be saved
data_dir = "./Selection_Tests"
output_dir = "./Selection_Tests/plots"
os.makedirs(output_dir, exist_ok=True)

# Read the .csv file
data_file = os.path.join(data_dir, "Rate_comparisons_between_50KB_and_others.csv")
data = pd.read_csv(data_file)

# Define symbols for different Gene_groups
markers = {"NuCpRP": "s", "CpRP": "o", "NuCyRP": "^", "NuCpOT": "D", "CpPS": "p"}
colors = {"CpRP": "blue", "NuCpRP": "orange", "NuCpOT": "green", "NuCyRP": "red", "CpPS": "purple"}

# Create a scatter plot and capture the axes object
plt.figure(figsize=(10, 8))
ax = sns.scatterplot(data=data, x="dN_dS_basal_Legumes", y="dN_dS_50KB", hue="Gene_group", style="Gene_group", markers=markers, palette=colors)

# Add a 1:1 dashed line
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]
ax.plot(lims, lims, 'k--', alpha=0.75)

# Remove the legend
ax.legend_.remove()

# Save the figure before showing it
output_file = os.path.join(output_dir, "inset_seaborn_legend_removed.png")
plt.savefig(output_file, dpi=300)

# Show the plot
plt.show()

print(f"Plot saved as {output_file}")
