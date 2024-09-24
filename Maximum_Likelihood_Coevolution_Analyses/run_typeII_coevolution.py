# run_typeII_coevolution.py
# This script calculates the Type II coevolution statistic for CpRP and NuCpRP genes

import csv

# Load the codon substitution data (input file format should be adjusted)
with open("codon_substitutions.csv", "r") as infile:
    reader = csv.reader(infile)
    codon_data = list(reader)

# Initialize variables for calculating the Type II coevolution statistic
num_pairs = 0
branch_distances_sum = 0

# Iterate through the data to calculate the number of pairs and branch distances
for codon_pair in codon_data:
    # Assuming codon_pair format [CpRP_substitutions, NuCpRP_substitutions, branches_separating]
    CpRP_sub, NuCpRP_sub, branches_separating = codon_pair
    num_pairs += 1
    branch_distances_sum += int(branches_separating)

# Calculate the Type II coevolution statistic (average branch distance between consecutive pairs)
typeII_statistic = branch_distances_sum / num_pairs if num_pairs > 0 else 0

# Output the result
print(f"Type II coevolution statistic (average branches separating substitutions): {typeII_statistic}")
