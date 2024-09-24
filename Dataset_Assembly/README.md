# Dataset_Assembly
This directory contains scripts and methods for assembling the datasets used in the manuscript. Below is a breakdown of each step in the assembly pipeline including raw read quality control, adapter trimming, rRNA removal, transcriptome assembly, and sequence extraction.

### Contents
- ```run_fastqc.sh```: Quality control of raw RNA-seq reads using FastQC.
- ```run_trimgalore.sh```: Adapter trimming and low-quality read filtering using TrimGalore.
- ```run_sortmerna.sh```: Ribosomal RNA removal using SortMeRNA.
- ```run_trinity.sh```: Transcriptome assembly using Trinity.
- ```extract_align_genes.sh```: Gene extraction and alignment using BLAST and MAFFT.

### Step-by-Step Breakdown
**1. Quality Control**
**Script:** ```run_fastqc.sh```
**Tool:** FastQC v.0.11.5
