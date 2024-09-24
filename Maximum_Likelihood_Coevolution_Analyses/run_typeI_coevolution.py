# run_typeI_coevolution.py
# This script calculates the Type I coevolution statistic for CpRP and NuCpRP genes

import csv

# Load the codon substitution data (input file format should be adjusted)
with open("codon_substitutions.csv", "r") as infile:
    reader = csv.reader(infile)
    codon_data = list(reader)

# Initialize counters for codons with substitutions on 1, 2, or 3 branches
one_branch = 0
two_branches = 0
three_branches = 0

# Iterate through the data to calculate the coevolution statistic
for codon_pair in codon_data:
    # Assuming codon_pair format [CpRP_substitutions, NuCpRP_substitutions, branches]
    CpRP_sub, NuCpRP_sub, branches = codon_pair
    if branches == "1":
        one_branch += 1
    elif branches == "2":
        two_branches += 1
    elif branches == "3":
        three_branches += 1

# Output the results
print(f"Codons with substitutions on 1 branch: {one_branch}")
print(f"Codons with substitutions on 2 branches: {two_branches}")
print(f"Codons with substitutions on 3 branches: {three_branches}")
