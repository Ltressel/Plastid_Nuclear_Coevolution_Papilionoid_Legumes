#!/bin/bash
# run_codeml_coevolution.sh
# This script runs PAML (CODEML) to reconstruct ancestral codons using the F3 × 4 codon model

# Define input files and directories
CTL_FILE="codeml_coevolution.ctl"  # <<< Update with your control file
OUTPUT_DIR="paml_output"
mkdir -p $OUTPUT_DIR

# Run PAML (CODEML) with the control file
echo "Running CODEML for ancestral codon reconstruction..."
codeml $CTL_FILE

# Move output files to the specified output directory
mv rst $OUTPUT_DIR/
mv rst1 $OUTPUT_DIR/
mv 2ML.t $OUTPUT_DIR/
mv 2ML.b $OUTPUT_DIR/

# Output message
echo "Ancestral codon reconstruction complete. Results saved in $OUTPUT_DIR."
