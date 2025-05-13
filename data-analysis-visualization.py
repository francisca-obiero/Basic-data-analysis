import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Task 1: Load and Explore the Dataset

print("Current working directory:", os.getcwd())

file_path = 'todays_data.csv'  # Ensure this file is in the same folder as your script

try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the file name and location.")
    exit()

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Print actual column names
print("\nColumns in dataset:", data.columns.tolist())

print("\nFirst 5 rows of the dataset:")
print(data.head())

print("\nDataset info:")
print(data.info())

print("\nMissing values per column:")
print(data.isnull().sum())

# Clean the dataset by dropping rows with missing values
data = data.dropna()
print("\nDataset after dropping missing values:")
print(data.head())

# Task 2: Basic Data Analysis (Categorical)

# Choose categorical columns for grouping and counts
group_column = 'Country'        # Example categorical column
second_group_column = 'Gender'  # Another categorical column for grouping

# Count of entries per category in group_column
category_counts = data[group_column].value_counts()
print(f"\nCounts per {group_column}:")
print(category_counts)

# Cross-tabulation of two categorical columns
cross_tab = pd.crosstab(data[group_column], data[second_group_column])
print(f"\nCross-tabulation of {group_column} and {second_group_column}:")
print(cross_tab)

# Task 3: Data Visualization (Categorical)

# 1. Count plot for Gender distribution
plt.figure(figsize=(8,5))
sns.countplot(data=data, x=second_group_column, order=data[second_group_column].value_counts().index)
plt.title(f'Count of each {second_group_column}')
plt.xlabel(second_group_column)
plt.ylabel('Count')
plt.show()

# 2. Bar chart for counts of Country
plt.figure(figsize=(8,5))
category_counts.plot(kind='bar', color='skyblue')
plt.title(f'Count of entries per {group_column}')
plt.xlabel(group_column)
plt.ylabel('Count')
plt.show()

# 3. Stacked bar chart: Gender counts per Country
plt.figure(figsize=(10,6))
cross_tab.plot(kind='bar', stacked=True)
plt.title(f'{second_group_column} Counts per {group_column}')
plt.xlabel(group_column)
plt.ylabel('Count')
plt.legend(title=second_group_column)
plt.show()

# 4. Pie chart for Academic Level distribution
if 'Academic Level' in data.columns:
    plt.figure(figsize=(7,7))
    data['Academic Level'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Academic Level')
    plt.ylabel('')  # Hide y-label for pie chart
    plt.show()
else:
    print("Column 'Academic Level' not found. Skipping pie chart.")
