"""
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Project: Statistical Data Analysis with Seaborn

Data Generator Script
This script generates synthetic data for statistical analysis and visualization.
"""

import numpy as np
import pandas as pd

def generate_statistical_data(n_samples=1000, random_seed=42):
    """
    Generate synthetic dataset for statistical analysis.
    
    Parameters:
    -----------
    n_samples : int
        Number of samples to generate
    random_seed : int
        Random seed for reproducibility
    
    Returns:
    --------
    pd.DataFrame
        Generated dataset with multiple variables
    """
    np.random.seed(random_seed)
    
    # Create a dataset with multiple variables
    data = {
        'Age': np.random.normal(35, 10, n_samples),
        'Income': np.random.normal(50000, 15000, n_samples),
        'Spending': np.random.normal(3000, 800, n_samples),
        'Satisfaction': np.random.normal(7.5, 1.5, n_samples),
        'Experience': np.random.normal(5, 3, n_samples),
        'Category': np.random.choice(['A', 'B', 'C'], n_samples)
    }
    
    # Add some correlations
    data['Income'] = data['Income'] + data['Age'] * 500
    data['Spending'] = data['Spending'] + data['Income'] * 0.05 + np.random.normal(0, 200, n_samples)
    data['Satisfaction'] = np.clip(data['Satisfaction'] + (data['Income'] - 50000) / 20000, 1, 10)
    
    df = pd.DataFrame(data)
    
    # Ensure positive values
    df['Age'] = np.abs(df['Age'])
    df['Income'] = np.abs(df['Income'])
    df['Spending'] = np.abs(df['Spending'])
    df['Experience'] = np.abs(df['Experience'])
    
    return df

if __name__ == "__main__":
    # Generate and save dataset
    df = generate_statistical_data()
    df.to_csv('statistical_data.csv', index=False)
    print("Dataset generated and saved as 'statistical_data.csv'")
    print(f"Shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nStatistical Summary:")
    print(df.describe())

