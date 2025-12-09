"""
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Project: Statistical Data Analysis with Seaborn

Main script to run all statistical visualizations.
This script can be used as an alternative to the Jupyter notebook.
"""

import pandas as pd
from data_generator import generate_statistical_data
from visualization_utils import (
    setup_plot_style,
    create_correlation_heatmap,
    create_distribution_plots,
    create_box_plots,
    create_violin_plots,
    create_pair_plot,
    print_statistical_summary
)

def main():
    """
    Main function to generate data and create all visualizations.
    """
    print("=" * 60)
    print("Statistical Data Analysis with Seaborn")
    print("Author: RSK World")
    print("Website: https://rskworld.in")
    print("=" * 60)
    print("\nGenerating dataset...")
    
    # Generate or load data
    try:
        df = pd.read_csv('statistical_data.csv')
        print("Loaded existing dataset from 'statistical_data.csv'")
    except FileNotFoundError:
        print("Generating new dataset...")
        df = generate_statistical_data()
        df.to_csv('statistical_data.csv', index=False)
        print("Dataset saved as 'statistical_data.csv'")
    
    print(f"Dataset shape: {df.shape}")
    print("\nSetting up plot style...")
    setup_plot_style()
    
    # Define variables for visualization
    numeric_vars = ['Age', 'Income', 'Spending', 'Satisfaction']
    category_col = 'Category'
    
    print("\nCreating visualizations...")
    print("\n1. Correlation Matrix Heatmap...")
    create_correlation_heatmap(df, save_path='correlation_heatmap.png')
    
    print("\n2. Distribution Plots...")
    create_distribution_plots(df, numeric_vars, save_path='distribution_plots.png')
    
    print("\n3. Box Plots...")
    create_box_plots(df, numeric_vars, category_col, save_path='box_plots.png')
    
    print("\n4. Violin Plots...")
    create_violin_plots(df, numeric_vars, category_col, save_path='violin_plots.png')
    
    print("\n5. Pair Plot...")
    create_pair_plot(df, numeric_vars, category_col, save_path='pair_plot.png')
    
    print("\n6. Statistical Summary...")
    print_statistical_summary(df)
    
    print("\n" + "=" * 60)
    print("All visualizations completed successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    print("- correlation_heatmap.png")
    print("- distribution_plots.png")
    print("- box_plots.png")
    print("- violin_plots.png")
    print("- pair_plot.png")
    print("\nProject by: RSK World")
    print("Website: https://rskworld.in")

if __name__ == "__main__":
    main()

