#!/bin/bash
# run_trimgalore.sh
# Trim adapters and low-quality bases from raw RNA-seq reads

# Create output directory if it doesn't exist
mkdir -p trimmed_reads

# Run TrimGalore on all paired-end .fastq.gz files
for file in *_R1_*.fastq.gz; do
    base=$(basename $file "_R1_*.fastq.gz")
    trim_galore --paired ${base}_R1_*.fastq.gz ${base}_R2_*.fastq.gz -o trimmed_reads/
done

# Output message when completed
echo "Trimming complete. Results saved in trimmed_reads/"
