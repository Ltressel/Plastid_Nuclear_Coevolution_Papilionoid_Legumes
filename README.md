# Plastid_Nuclear_Coevolution_Papilionoid_Legumes
## Overview
This repository contains descriptions of scripts and bioinformatic pipelines used for the manuscript **"Plastid-Nuclear Coevolution of Ribosomal Protein Genes in Papilionoid Legumes"** by Tressel et al. The study investigates plastid-nuclear coevolution by analyzing ribosomal protein genes encoded by both plastid and nuclear genomes across 52 taxa of the legume family Fabaceae. This research provides insight into how maximum likelihood methods and evolutionary rate covariation between nuclear and plastid genomes may drive cytonuclear coevolution, with implications for plant diversification and crop improvement. 

## Repository Contents
- ```Dataset_Assembly/```: This directory contains scripts and methods for assembling the datasets used in the study, including raw read quality control, adapter trimming, rRNA removal, transcriptome assembly, and sequence extraction. 
- ```Substitution_Rate_Estimation/```: This directory contains scripts for estimating nonsynonymous (*dN*) and synonymous (*dS*) substitution rates using PAML (CODEML) and HyPhy, along with methods for Wilcoxon tests and boxplot generation. 
- ```Selection_Tests/```:  This directory contains scripts for detecting positive and relaxed selection using PAML (CODEML) and HyPhy (RELAX).
- ```Evolutionary_Rate_Covariation_Analyses/```: This directory contains scripts for performing evolutionary rate covariation (ERC) analysis, testing correlations between plastid and nuclear gene sets. 
- ```Maximum_Likelihood_Coevolution_Analyses/```: This directory contains scripts for investigating coevolution between CpRP and NuCpRP genes using maximum likelihood methods, calculating Type I and Type II coevolution statistics, and visualizing the results in a matrix heatmap.

## Key Findings
- Elevated nonsynonymous substitution rates (*dN*) and nonsynonymous/synonymous substitution rate ratios (*dN/dS*) in plastid-encoded and nuclear-encoded plastid-targeted ribosomal protein genes.
- Significant differences in *dN* for CpRP and NuCpRP substitution rates between the 50-kb inversion clade and other legumes.
- Strong signals of cytonuclear coevolution were identified using maximum likelihood methods and evolutionary rate covariation analysis, with evidence of coordinated evolution between plastid- and nuclear-encoded ribosomal protein genes in the 50-kb clade.

## Impact
The findings of this study on plastid-nuclear coevolution have significant implications for plant biology and crop improvement. By elucidating how ribosomal protein genes encoded by plastid and nuclear genomes have coevolved, particularly in the 50-kb inversion clade of legumes, this research provides critical insights into the molecular mechanisms underlying plant diversification and adaptation.

- **Enhanced Understanding of Cytonuclear Interactions:** The coevolution of plastid and nuclear genomes plays a crucial role in cellular processes, including protein synthesis and photosynthesis, which are essential for plant growth and productivity. Understanding these interactions can lead to targeted breeding strategies that enhance these fundamental functions.

- **Identification of Key Genetic Targets:** The coevolutionary relationships identified between plastid-encoded and nuclear-encoded ribosomal protein genes provide valuable genetic targets for improving stress tolerance, growth efficiency, and resource use in crops. By focusing on genes with significant cytonuclear interaction, breeding programs can select for traits that improve crop resilience and yield.

- **Application to Legume Crops:** As legumes are a key source of protein and nitrogen fixation in agricultural systems, understanding their unique genomic adaptations can facilitate the development of more robust legume varieties. This research can directly contribute to enhancing traits such as nitrogen efficiency, drought resistance, and pest tolerance in economically important legume crops like soybeans, peanuts, and lentils.

- **Broader Applications to Other Crops:** While this study focuses on papilionoid legumes, the insights gained into cytonuclear coevolution are broadly applicable to other crop taxa. These findings could inform breeding strategies in a wide range of plant species, promoting more sustainable agricultural practices by optimizing plant growth and adaptability in changing environments.

## Methods
- Constraint tree contruction using RAxML
- Substitution rate estimation using PAML and LRTs
- Positive selection tests using LRTs and PAML
- Relaxed selection tests using Hyphy
- Evolutionary rate covariation analyses using normalized branch length tests to assess coevolution
- Maximum likelihood analyses to assess coevolution using PAML

## Citation
- Tressel L.G., Shrestha B., Lee C., Choi I.-S., Ruhlman T.A., Cardoso D., Wojciechowski M.F., Jansen R.K. 2024. Plastid-nuclear coevolution of ribosomal genes in papilionoid legumes.  Molecular Phylogenetics and Evolution, in review.

## Acknowledgements
We thank the TEX-LL, HUEFS, and RB herbaria for voucher deposition, the Desert Legume Program at the University of Arizona for seeds.  We also thank George Yatskievych (TEX/LL) for arranging a formal Material Transfer Agreement (Decree number 8772) under the SisGen Cadastro RDC6BE9, which facilitated research activities between our institutions. Finally, we thank Luciano P. de Queiroz (HUEFS) and Haroldo C. de Lima (RB) for providing access to living collections and for arranging field work in Brazil.

## Funding sources list
This work was supported by grants from the National Science Foundation (DEB-1853010 and DEB-1853024) to MW, RJ, and TR, the Texas Ecological Laboratory Program (EcoLab) to RJ, TR, and I-SC, the Sidney F. and Doris Blake Professorship in Systematic Botany to RJ, the CNPq (Research Productivity Fellowship no. 308244/2018-4; Universal no. 422325/2018-0), FAPESB (Universal no. APP0037/2016), and UFBA PROQUAD program to DC.
