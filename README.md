# Statistical Data Analysis with Seaborn

**Author:** RSK World  
**Website:** https://rskworld.in  
**Email:** help@rskworld.in  
**Phone:** +91 93305 39277  

## Project Description

Comprehensive statistical visualization project with advanced plotting techniques using Seaborn for data analysis and exploration. This project demonstrates advanced statistical visualization techniques including correlation matrices, distribution plots, box plots, violin plots, pair plots, and heatmaps. Perfect for exploratory data analysis and statistical insights.

## Features

- **Correlation matrix heatmaps** - Understanding relationships between variables
- **Distribution and density plots** - Analyzing data distributions
- **Box plots and violin plots** - Identifying quartiles, outliers, and distributions
- **Pair plots for multivariate analysis** - Comprehensive pairwise variable analysis
- **Statistical summary visualizations** - Comprehensive statistical overview
- **Categorical plots** - Count plots and bar plots with error bars
- **Regression plots** - With confidence intervals for relationship analysis
- **Facet grids** - Multi-panel visualizations for grouped data
- **Q-Q plots** - Normality testing and distribution validation
- **Clustermap** - Hierarchical clustering visualization
- **Residual analysis** - Regression diagnostics and model validation
- **Ridge plots (Joy plots)** - Overlapping density distributions
- **Time series analysis** - Temporal data visualization
- **Advanced heatmaps** - Pivot table visualizations with annotations

## Technologies Used

- Python
- Seaborn
- Matplotlib
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Jupyter Notebook

## Difficulty Level

Intermediate

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Jupyter Notebook

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `statistical_analysis.ipynb` and run all cells

### Option 2: Python Scripts

1. Generate data:
```bash
python data_generator.py
```

2. Use visualization utilities in your own scripts:
```python
from visualization_utils import *
import pandas as pd

# Load or generate data
df = pd.read_csv('statistical_data.csv')

# Setup plot style
setup_plot_style()

# Create visualizations
create_correlation_heatmap(df)
create_distribution_plots(df, ['Age', 'Income', 'Spending', 'Satisfaction'])
create_box_plots(df, ['Age', 'Income'], 'Category')
create_violin_plots(df, ['Age', 'Income'], 'Category')
create_pair_plot(df, ['Age', 'Income', 'Spending', 'Satisfaction'], 'Category')
```

## Project Structure

```
statistical-seaborn/
├── statistical_analysis.ipynb    # Main Jupyter notebook with all visualizations
├── data_generator.py              # Script to generate synthetic data
├── create_example_data.py         # Script to create comprehensive example dataset
├── visualization_utils.py        # Utility functions for visualizations
├── main.py                        # Main script to run all visualizations
├── requirements.txt               # Python package dependencies
├── README.md                      # Project documentation
├── LICENSE                        # MIT License file
├── setup.py                       # Setup script for package installation
├── index.html                     # Demo page
├── statistical_data.csv            # Generated dataset (created after running data_generator.py)
└── example_data.csv               # Comprehensive example dataset (created after running create_example_data.py)
```

## Visualizations Included

1. **Correlation Matrix Heatmap** - Visual representation of correlations between all numeric variables
2. **Distribution Plots** - Histograms with KDE (Kernel Density Estimation) for each variable
3. **Density Plots by Category** - Overlaid density plots showing distributions across categories
4. **Box Plots** - Quartile analysis and outlier detection by category
5. **Violin Plots** - Combination of box plot and density plot information
6. **Pair Plots** - Scatter plot matrix for multivariate analysis
7. **Statistical Summary Visualizations** - Bar charts and heatmaps of statistical measures
8. **Advanced Visualizations** - Joint plots, strip plots, and swarm plots
9. **Categorical Count Plots** - Frequency analysis of categorical variables
10. **Bar Plots with Error Bars** - Mean values with standard deviation indicators
11. **Regression Plots** - Scatter plots with regression lines and confidence intervals
12. **Facet Grid Visualizations** - Multi-panel plots for grouped analysis
13. **Q-Q Plots** - Quantile-quantile plots for normality testing
14. **Clustermap** - Hierarchical clustering heatmap with dendrograms
15. **Residual Analysis** - Comprehensive regression diagnostic plots
16. **Ridge Plots** - Overlapping density distributions (Joy plots)
17. **Time Series Analysis** - Temporal trends and patterns visualization
18. **Pivot Table Heatmaps** - Cross-tabulation visualizations

## Statistical Analysis

The project includes:
- Correlation analysis
- Descriptive statistics
- Category-wise statistics
- Skewness and kurtosis calculations
- Bivariate analysis with regression lines

## Output

All visualizations are saved as high-resolution PNG images (300 DPI) with descriptive filenames:
- `correlation_heatmap.png`
- `distribution_plots.png`
- `density_plots.png`
- `box_plots.png`
- `box_plots_all.png`
- `violin_plots.png`
- `pair_plot.png`
- `pair_plot_regression.png`
- `statistical_summary.png`
- `summary_heatmap.png`
- `joint_plots.png`
- `strip_swarm_plots.png`
- `categorical_count_plots.png`
- `bar_plots_error_bars.png`
- `regression_plots.png`
- `facet_grid_distribution.png`
- `facet_grid_scatter.png`
- `qq_plots.png`
- `clustermap.png`
- `residual_analysis.png`
- `ridge_plots.png`
- `time_series_analysis.png`
- `heatmap_pivot.png`
- `heatmap_satisfaction.png`

## License

This project is provided as-is for educational and demonstration purposes.

## Contact

For questions, suggestions, or support, please contact:

**RSK World**  
Website: https://rskworld.in  
Email: help@rskworld.in  
Phone: +91 93305 39277

---

**Note:** This project is part of the RSK World collection of free programming resources and source code.

