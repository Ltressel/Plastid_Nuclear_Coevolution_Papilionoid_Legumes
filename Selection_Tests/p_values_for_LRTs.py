import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the directory where the CSV file is located and the output will be saved
data_dir = "./Selection_Tests"
output_dir = "./Selection_Tests/plots"
os.makedirs(output_dir, exist_ok=True)

# Read the .csv file
data_file = os.path.join(data_dir, "p_values_LRT.csv")
data = pd.read_csv(data_file)

# Sort the data by the "number" column in ascending order
data = data.sort_values(by="number")

# Define symbols for different Gene_groups
markers = {"NuCpRP": "s", "CpRP": "o", "NuCyRP": "^", "NuCpOT": "D", "CpPS": "p"}
colors = {"CpRP": "blue", "NuCpRP": "orange", "NuCpOT": "green", "NuCyRP": "red", "CpPS": "purple"}

# Set the figure size
plt.figure(figsize=(15, 10))

# Create the scatter plot using seaborn
sns.scatterplot(data=data, x="number", y="Gene", hue="Gene_group", style="Gene_group", markers=markers, palette=colors)

# Add a vertical dashed line at -1.3
plt.axvline(-1.3, linestyle='--', color='gray')

# Customize the plot
plt.xlabel("log p-value", fontsize=14)
plt.ylabel('')  # Remove y-axis label

# Make legend larger by setting the fontsize parameter
plt.legend(fontsize=15)

# Remove ticks and labels from the y-axis
plt.yticks([])

# Save the figure before showing it
output_file = os.path.join(output_dir, "scatter_plot_seaborn.png")
plt.savefig(output_file, dpi=300)

# Show the plot
plt.show()

print(f"Plot saved as {output_file}")
