import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import Normalize

# Load the Excel file containing p-values for coevolution analyses
df = pd.read_excel('Figure_Coevolution_Analyses_3.xlsx')

# Specify the order of values for 'Leading' and 'Trailing'
order_leading = ['PSRP-1', 'PSRP-2', 'RPL1', 'RPL11', 'RPL13', 'RPL15', 'RPL17', 'RPL18-1',
                 'RPL18-2', 'RPL19', 'RPL21', 'RPL24', 'RPL27', 'RPL28', 'RPL29',
                 'RPL3', 'RPL31', 'RPL34', 'RPL35', 'RPL4', 'RPL5', 'RPL6', 'RPS1',
                 'RPS10', 'RPS13', 'RPS20', 'RPS5', 'RPS6', 'RPS9', 'rpl14', 'rpl16',
                 'rpl2', 'rpl32', 'rpl36', 'rps11', 'rps12', 'rps14', 'rps15', 'rps18',
                 'rps19', 'rps2', 'rps3', 'rps4', 'rps7', 'rps8', 'rpl23']

order_trailing = ['rpl23', 'rps8', 'rps7', 'rps4', 'rps3', 'rps2',
                  'rps19', 'rps18', 'rps15', 'rps14', 'rps12', 'rps11', 'rpl36', 'rpl32',
                  'rpl2', 'rpl16', 'rpl14', 'RPS9', 'RPS6', 'RPS5', 'RPS20', 'RPS13',
                  'RPS10', 'RPS1', 'RPL6', 'RPL5', 'RPL4', 'RPL35', 'RPL34', 'RPL31',
                  'RPL3', 'RPL29', 'RPL28', 'RPL27', 'RPL24', 'RPL21', 'RPL19',
                  'RPL18-2', 'RPL18-1', 'RPL17', 'RPL15', 'RPL13', 'RPL11', 'RPL1', 'PSRP-2', 'PSRP-1']

# Convert 'Leading' and 'Trailing' to ordered categorical types
df['Leading'] = pd.Categorical(df['Leading'].str.replace('RPL18_1', 'RPL18-1').str.replace('RPL18_2', 'RPL18-2'),
                               categories=order_leading, ordered=True)
df['Trailing'] = pd.Categorical(df['Trailing'].str.replace('RPL18_1', 'RPL18-1').str.replace('RPL18_2', 'RPL18-2'),
                                categories=order_trailing[::-1], ordered=True)

# Sort DataFrame by 'Leading' and 'Trailing'
df.sort_values(['Leading', 'Trailing'], inplace=True)

# Create a matrix using pivot_table
matrix = df.pivot_table(index='Trailing', columns='Leading', values='p-value', aggfunc='first')

# Create a custom colormap
cmap = LinearSegmentedColormap.from_list(
    name='custom', 
    colors=['blue', 'white', 'lightgray'], 
    N=100
)

# Define a normalizer with the correct cut-off for p=0.05
norm = Normalize(vmin=0, vmax=0.05, clip=True)

# Plot the matrix as a heatmap
plt.figure(figsize=(20, 15))
ax = sns.heatmap(matrix, cmap=cmap, norm=norm, annot=False, cbar_kws={"shrink": 0.5, 'label': 'p-value'})

# Move color bar closer to the figure
ax.figure.axes[-1].xaxis.labelpad = 30

# Set x-axis tick labels
plt.xticks(range(len(order_leading)), order_leading, rotation='vertical')

# Remove x-axis and y-axis labels
plt.xlabel('')
plt.ylabel('')

# Save the figure
plt.savefig('Matrix_of_p_values.png')

# Show the figure
plt.show()
