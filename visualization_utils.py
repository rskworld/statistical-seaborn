"""
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Project: Statistical Data Analysis with Seaborn

Visualization Utilities
Helper functions for creating statistical visualizations with Seaborn.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def setup_plot_style():
    """
    Set up the default plotting style for all visualizations.
    """
    sns.set_style("whitegrid")
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10

def create_correlation_heatmap(df, numeric_cols=None, figsize=(12, 10), save_path=None):
    """
    Create a correlation matrix heatmap.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_cols : list, optional
        List of numeric column names. If None, auto-detect.
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save the figure
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    correlation_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                square=True,
                linewidths=1,
                cbar_kws={"shrink": 0.8},
                fmt='.2f')
    plt.title('Correlation Matrix Heatmap\nStatistical Data Analysis with Seaborn - RSK World', 
              fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def create_distribution_plots(df, variables, figsize=(15, 12), save_path=None):
    """
    Create distribution plots for multiple variables.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    variables : list
        List of variable names to plot
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save the figure
    """
    n_vars = len(variables)
    n_cols = 2
    n_rows = (n_vars + 1) // 2
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle('Distribution and Density Plots\nStatistical Data Analysis with Seaborn - RSK World', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    axes_flat = axes.flatten()
    
    for idx, var in enumerate(variables):
        sns.histplot(data=df, x=var, kde=True, ax=axes_flat[idx], bins=30)
        axes_flat[idx].set_title(f'Distribution of {var}', fontweight='bold')
        axes_flat[idx].set_xlabel(var)
        axes_flat[idx].set_ylabel('Frequency')
        axes_flat[idx].grid(True, alpha=0.3)
    
    # Hide unused subplots
    for idx in range(n_vars, len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def create_box_plots(df, variables, category_col, figsize=(15, 12), save_path=None):
    """
    Create box plots for variables by category.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    variables : list
        List of variable names to plot
    category_col : str
        Name of the category column
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save the figure
    """
    n_vars = len(variables)
    n_cols = 2
    n_rows = (n_vars + 1) // 2
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle('Box Plots by Category\nStatistical Data Analysis with Seaborn - RSK World', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    axes_flat = axes.flatten()
    
    for idx, var in enumerate(variables):
        sns.boxplot(data=df, x=category_col, y=var, ax=axes_flat[idx])
        axes_flat[idx].set_title(f'Box Plot of {var} by Category', fontweight='bold')
        axes_flat[idx].set_xlabel('Category')
        axes_flat[idx].set_ylabel(var)
        axes_flat[idx].grid(True, alpha=0.3, axis='y')
    
    # Hide unused subplots
    for idx in range(n_vars, len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def create_violin_plots(df, variables, category_col, figsize=(15, 12), save_path=None):
    """
    Create violin plots for variables by category.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    variables : list
        List of variable names to plot
    category_col : str
        Name of the category column
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save the figure
    """
    n_vars = len(variables)
    n_cols = 2
    n_rows = (n_vars + 1) // 2
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle('Violin Plots by Category\nStatistical Data Analysis with Seaborn - RSK World', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    axes_flat = axes.flatten()
    
    for idx, var in enumerate(variables):
        sns.violinplot(data=df, x=category_col, y=var, ax=axes_flat[idx], inner='box')
        axes_flat[idx].set_title(f'Violin Plot of {var} by Category', fontweight='bold')
        axes_flat[idx].set_xlabel('Category')
        axes_flat[idx].set_ylabel(var)
        axes_flat[idx].grid(True, alpha=0.3, axis='y')
    
    # Hide unused subplots
    for idx in range(n_vars, len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def create_pair_plot(df, variables, hue_col=None, save_path=None):
    """
    Create a pair plot for multivariate analysis.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    variables : list
        List of variable names to plot
    hue_col : str, optional
        Column name for color coding
    save_path : str, optional
        Path to save the figure
    """
    plot_data = df[variables + ([hue_col] if hue_col else [])]
    
    pair_plot = sns.pairplot(plot_data, 
                             hue=hue_col if hue_col else None,
                             diag_kind='kde',
                             plot_kws={'alpha': 0.6},
                             height=2.5)
    pair_plot.fig.suptitle('Pair Plot for Multivariate Analysis\nStatistical Data Analysis with Seaborn - RSK World', 
                           fontsize=16, fontweight='bold', y=1.02)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def print_statistical_summary(df, numeric_cols=None):
    """
    Print comprehensive statistical summary.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_cols : list, optional
        List of numeric column names. If None, auto-detect.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    print("=" * 60)
    print("STATISTICAL INSIGHTS")
    print("=" * 60)
    print("\n1. CORRELATION ANALYSIS:")
    print(df[numeric_cols].corr())
    
    print("\n\n2. DESCRIPTIVE STATISTICS:")
    print(df[numeric_cols].describe())
    
    print("\n\n3. SKEWNESS AND KURTOSIS:")
    for col in numeric_cols:
        skewness = stats.skew(df[col])
        kurtosis = stats.kurtosis(df[col])
        print(f"{col}: Skewness = {skewness:.3f}, Kurtosis = {kurtosis:.3f}")
    
    print("\n" + "=" * 60)

