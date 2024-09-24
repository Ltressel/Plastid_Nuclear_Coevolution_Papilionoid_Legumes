# Maximum_Likelihood_Coevolution_Analyses
This directory contains scripts and methods for performing maximum likelihood coevolution analyses to investigate whether nonsynonymous substitutions in CpRP and NuCpRP genes tend to coincide along the same branches of the phylogenetic tree, and whether these substitutions occur sequentially more often than expected under a null hypothesis.

### Contents
- ```run_codeml_coevolution.sh``` Script to run **PAML (CODEML)** for ancestral codon reconstruction using the F3 × 4 codon model.
- ```run_typeI_coevolution.py```: Python script for calculating the Type I coevolution statistic based on codons with nonsynonymous substitutions.
- ```run_typeII_coevolution.py```: Python script for calculating the Type II coevolution statistic based on the number of branches separating consecutive nonsynonymous substitutions.
