# Substitution_Rate_Estimation

This directory contains scripts and methods for estimating the nonsynonymous (*dN*) and synonymous (*dS*) substitution rates for genes in the study. The analyses were conducted using **PAML v4.7** and **HyPhy**, with likelihood ratio tests (LRTs) to compare substitution rates between branches.

### Contents
- ```run_codeml.sh```: Script to run PAML (CODEML) for estimating *dN*, *dS*, *dN/dS*, and performing LRTs.
- ```run_hyphy.sh```: Script to run HyPhy with the MG94xHKY85 codon model.
- ```run_wilcoxon_test.R```: R script for performing Wilcoxon rank sum tests on the *dN* and *dS* values.
- ```generate_boxplots.R```: R script for generating boxplots of *dN* and *dS*, and combining them into a single figure.

### Step
