# visualize_erc_results.R
# This script visualizes the distribution of bootstrapped Spearman correlations between CpRP and nuclear-encoded gene sets

# Load necessary libraries
library(ggplot2)

# Set working directory (optional)
# setwd("path_to_directory")  # <<< Update if necessary

# Step 1: Load the bootstrapped correlation data for visualization
# Assume the bootstrapped correlations are stored for CpRP vs each nuclear-encoded gene set
bootstrapped_correlations <- read.csv("bootstrap_results.csv")  # <<< Update with the actual file

# Function to plot bootstrapped correlation distribution for a gene pair
plot_bootstrap_distribution <- function(correlation_data, gene_group_name, file_name) {
  # Calculate mean and 95% confidence interval
  ci_low <- quantile(correlation_data, 0.025)
  ci_high <- quantile(correlation_data, 0.975)
  mean_corr <- mean(correlation_data)
  
  # Create data frame for ggplot
  boot_data <- data.frame(correlations = correlation_data)
  
  # Generate plot
  correlation_plot <- ggplot(boot_data, aes(x = correlations)) +
    geom_density(fill = "blue", alpha = 0.5) +
    geom_point(aes(x = mean_corr, y = 0), size = 4, color = "black") +  # Add mean point
    geom_errorbarh(aes(xmin = ci_low, xmax = ci_high, y = 0), height = 0.1, color = "black", size = 1) +  # Add horizontal error bars
    labs(title = paste("Distribution of Bootstrapped Correlations (", gene_group_name, ")", sep=""),
         x = "Bootstrapped Spearman Correlation Coefficients",
         y = "Density") +
    theme_minimal() +
    theme(
      plot.title = element_text(hjust = 0.5, face = "bold"),
      panel.grid = element_blank(),            # Remove grid lines
      panel.border = element_rect(color = "black", fill = NA)  # Add edge lines
    )
  
  # Print the plot
  print(correlation_plot)
  
  # Save the plot as a PNG
  ggsave(file_name, plot = correlation_plot, width = 8, height = 6, dpi = 300)
}

# Step 2: Generate plots for CpRP and each nuclear-encoded gene set
# CpRP vs NuCpRP
plot_bootstrap_distribution(bootstrapped_correlations$CpRP_NuCpRP, "CpRP and NuCpRP", "erc_bootstrap_CpRP_NuCpRP_plot.png")

# CpRP vs NuCyRP
plot_bootstrap_distribution(bootstrapped_correlations$CpRP_NuCyRP, "CpRP and NuCyRP", "erc_bootstrap_CpRP_NuCyRP_plot.png")

# CpRP vs NuCpOT
plot_bootstrap_distribution(bootstrapped_correlations$CpRP_NuCpOT, "CpRP and NuCpOT", "erc_bootstrap_CpRP_NuCpOT_plot.png")
