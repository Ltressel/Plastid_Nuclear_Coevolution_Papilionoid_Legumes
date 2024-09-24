# Selection_Tests
This directory contains scripts and methods for detecting positive and relaxed selection within the 50-kb clade. The analyses were conducted using **PAML (CODEML)** for positive selection tests and **HyPhy (RELAX)** for relaxed selection tests. Additionally, Python scripts are included for visualization of LRT p-values and *dN/dS* values.

### Contents
- ```run_codeml_positive_selection.sh```: Script for running PAML (CODEML) to detect positive selection using branch-site models.
- ```run_relax_hyphy.sh```: Script for running HyPhy (RELAX) to detect relaxed selection.
- ```p_values_for_LRTs.py```: Python script to visualize the p-values from the LRT results.
- ```Inset_dN_dS_Figure.py```: Python script to create visualizations for dN/dS values.
