# run_erc_analysis.R
# This script performs evolutionary rate covariation (ERC) analysis using Spearman rank correlations and bootstrap resampling

# Load necessary libraries
library(boot)
library(psych)

# Set working directory (optional)
# setwd("path_to_directory")  # <<< Update if necessary

# Step 1: Load the normalized branch length data for each gene set
data <- read.csv("normalized_branch_lengths.csv")  # <<< Update with your data file

# Step 2: Calculate Spearman rank correlations between CpRP and each nuclear-encoded gene set
erc_results <- corr.test(data$CpRP, data[, c("NuCpRP", "NuCyRP", "NuCpOT")], method = "spearman")

# Print correlation results
print("Spearman Correlation Results:")
print(erc_results)

# Step 3: Define a function to bootstrap the correlation estimates
bootstrap_corr <- function(data, indices, gene_set) {
  d <- data[indices, ]
  cor(d$CpRP, d[[gene_set]], method = "spearman")
}

# Step 4: Perform bootstrap for each nuclear-encoded gene set (e.g., 10,000 iterations)
set.seed(123)
boot_results_nucprp <- boot(data, statistic = bootstrap_corr, R = 10000, gene_set = "NuCpRP")
boot_results_nucyrp <- boot(data, statistic = bootstrap_corr, R = 10000, gene_set = "NuCyRP")
boot_results_nucpot <- boot(data, statistic = bootstrap_corr, R = 10000, gene_set = "NuCpOT")

# Step 5: Combine the bootstrap results into a single data frame
bootstrap_combined <- data.frame(
  CpRP_NuCpRP = boot_results_nucprp$t,
  CpRP_NuCyRP = boot_results_nucyrp$t,
  CpRP_NuCpOT = boot_results_nucpot$t
)

# Step 6: Output bootstrap results to a single CSV file
write.csv(bootstrap_combined, file = "bootstrap_results.csv", row.names = FALSE)

# Save ERC results separately (optional)
write.csv(erc_results$r, file = "erc_results.csv")  # Save Spearman correlation results

# Step 7: Optional - Plot bootstrap distributions (can be moved to visualization script)
hist(boot_results_nucprp$t, main = "Bootstrap Distribution (CpRP vs NuCpRP)", xlab = "Correlation", breaks = 30)
hist(boot_results_nucyrp$t, main = "Bootstrap Distribution (CpRP vs NuCyRP)", xlab = "Correlation", breaks = 30)
hist(boot_results_nucpot$t, main = "Bootstrap Distribution (CpRP vs NuCpOT)", xlab = "Correlation", breaks = 30)

# The bootstrap results are now ready for the visualization script.
