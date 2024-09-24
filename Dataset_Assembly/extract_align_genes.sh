#!/bin/bash
# extract_align_genes.sh
# Extract ribosomal protein genes using BLAST and align sequences with MAFFT

# Define paths for input files and output directories
TRANSCRIPTOME="trinity_output/Trinity.fasta"  # Update with the actual transcriptome file
DB="target_gene_db.fasta"                     # Update with your BLAST database of target genes
OUT_DIR="blast_output"
ALIGN_DIR="aligned_sequences"

# Create output directories if they don't exist
mkdir -p $OUT_DIR $ALIGN_DIR

# Run BLASTx to identify ribosomal protein genes
blastx -query $TRANSCRIPTOME -db $DB -out $OUT_DIR/blast_output.txt -outfmt 6

# Extract FASTA sequences of BLAST hits
awk '{print $1}' $OUT_DIR/blast_output.txt | xargs samtools faidx $TRANSCRIPTOME > $OUT_DIR/blast_hits.fasta

# Run MAFFT to align the extracted sequences
mafft --auto $OUT_DIR/blast_hits.fasta > $ALIGN_DIR/aligned_sequences.fasta

# Output message when completed
echo "Gene extraction and alignment complete. Results saved in $ALIGN_DIR/"
