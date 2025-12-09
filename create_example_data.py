"""
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Project: Statistical Data Analysis with Seaborn

Script to create a comprehensive example dataset with multiple variables
for statistical analysis and visualization.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def create_comprehensive_dataset(n_samples=1000, random_seed=42):
    """
    Create a comprehensive dataset with multiple variables for statistical analysis.
    
    Parameters:
    -----------
    n_samples : int
        Number of samples to generate
    random_seed : int
        Random seed for reproducibility
    
    Returns:
    --------
    pd.DataFrame
        Comprehensive dataset with multiple variables
    """
    np.random.seed(random_seed)
    
    # Generate base variables
    age = np.abs(np.random.normal(35, 10, n_samples))
    gender = np.random.choice(['Male', 'Female', 'Other'], n_samples, p=[0.48, 0.48, 0.04])
    region = np.random.choice(['North', 'South', 'East', 'West'], n_samples)
    education = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 
                                n_samples, p=[0.25, 0.40, 0.25, 0.10])
    
    # Create correlated variables
    income = np.abs(np.random.normal(50000, 15000, n_samples) + age * 500)
    experience = np.abs(np.random.normal(5, 3, n_samples))
    
    # Spending depends on income and age
    spending = np.abs(np.random.normal(3000, 800, n_samples) + income * 0.05 + 
                     np.random.normal(0, 200, n_samples))
    
    # Satisfaction depends on income and spending
    satisfaction = np.clip(np.random.normal(7.5, 1.5, n_samples) + 
                          (income - 50000) / 20000 + (spending - 3000) / 1000, 1, 10)
    
    # Additional variables
    credit_score = np.clip(np.random.normal(650, 100, n_samples) + 
                          (income - 50000) / 500, 300, 850)
    
    loan_amount = np.abs(np.random.normal(20000, 10000, n_samples) * 
                        (income / 50000) + np.random.normal(0, 5000, n_samples))
    
    # Time-based variable
    start_date = datetime(2020, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 1095)) for _ in range(n_samples)]
    
    # Category based on income
    category = pd.cut(income, bins=[0, 40000, 60000, 80000, np.inf], 
                     labels=['Low', 'Medium', 'High', 'Very High'])
    
    # Create DataFrame
    df = pd.DataFrame({
        'ID': range(1, n_samples + 1),
        'Date': dates,
        'Age': age,
        'Gender': gender,
        'Region': region,
        'Education': education,
        'Income': income,
        'Spending': spending,
        'Satisfaction': satisfaction,
        'Experience': experience,
        'Credit_Score': credit_score,
        'Loan_Amount': loan_amount,
        'Category': category.astype(str)
    })
    
    # Add some missing values (5% missing)
    missing_indices = np.random.choice(df.index, size=int(n_samples * 0.05), replace=False)
    df.loc[missing_indices, 'Credit_Score'] = np.nan
    
    return df

if __name__ == "__main__":
    # Create comprehensive dataset
    df = create_comprehensive_dataset(n_samples=1000)
    
    # Save to CSV
    df.to_csv('example_data.csv', index=False)
    
    print("=" * 60)
    print("Comprehensive Example Dataset Created")
    print("=" * 60)
    print(f"\nDataset shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print("\nFirst few rows:")
    print(df.head(10))
    print("\nDataset Info:")
    print(df.info())
    print("\nStatistical Summary:")
    print(df.describe())
    print("\nCategorical Variables Summary:")
    print(f"\nGender distribution:\n{df['Gender'].value_counts()}")
    print(f"\nRegion distribution:\n{df['Region'].value_counts()}")
    print(f"\nEducation distribution:\n{df['Education'].value_counts()}")
    print(f"\nCategory distribution:\n{df['Category'].value_counts()}")
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\n" + "=" * 60)
    print("Dataset saved as 'example_data.csv'")
    print("=" * 60)

