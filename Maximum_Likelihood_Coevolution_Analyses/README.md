# Maximum_Likelihood_Coevolution_Analyses
This directory contains scripts and methods for performing maximum likelihood coevolution analyses to investigate whether nonsynonymous substitutions in CpRP and NuCpRP genes tend to coincide along the same branches of the phylogenetic tree, and whether these substitutions occur sequentially more often than expected under a null hypothesis.

### Contents
- ```run_codeml_coevolution.sh``` Script to run **PAML (CODEML)** for ancestral codon reconstruction using the F3 × 4 codon model.
- ```run_typeI_coevolution.py```: Python script for calculating the Type I coevolution statistic based on codons with nonsynonymous substitutions.
- ```run_typeII_coevolution.py```: Python script for calculating the Type II coevolution statistic based on the number of branches separating consecutive nonsynonymous substitutions.
- ```generate_matrix_figure.py```: Python script for creating a heatmap of p-values from Type I coevolution statistics.

### Step-by-Step Breakdown
**1. Run PAML (CODEML) for Ancestral Codon Reconstruction**

**Script:** ```run_codeml_coevolution.sh```

**Tool:** [PAML v4.7](https://github.com/abacus-gene/paml)

**Description:** This script runs PAML (CODEML) to estimate the posterior probability of ancestral codons for each node in the phylogenetic tree using the F3 × 4 codon model.

**Usage:** ```bash run_codeml_coevolution.sh```

**2. Calculate Type I Coevolution Statistic**

**Script:** ```run_typeI_coevolution.py```

**Tool:** Python (with necessary libraries)

**Description:** This Python script calculates the Type I coevolution statistic, which counts the number of codons with nonsynonymous substitutions on one, two, or three branches between CpRP and NuCpRP gene pairs.

**Usage:** ```python run_typeI_coevolution.py```

**3. Calculate Type II Coevolution Statistic**

**Script:** ```run_typeII_coevolution.py```

**Tool:** Python (with necessary libraries)

**Description:** This Python script calculates the Type II coevolution statistic, which examines the number of branches separating consecutive nonsynonymous substitutions between CpRP and NuCpRP genes.

**4. Generate Heatmap for Type I Coevolution Statistic (Matrix Visualization)**

**Script:** ```generate_matrix_figure.py```

**Tool:** Python (with ```pandas```, ```seaborn```, ```matplotlib```, and ```numpy```)

**Description:** This script generates a heatmap of the Type I coevolution statistic p-values between leading and trailing proteins, based on the data generated in this study

**Usage:** ```python run_typeII_coevolution.py```

