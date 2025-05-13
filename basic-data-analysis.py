import pandas as pd

# Load the dataset
file_path = 'your_dataset.csv'  # Replace with your dataset path
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Display the first few rows
print(data.head())

# Check data types and missing values
print(data.info())
print("\nMissing values:\n", data.isnull().sum())

# Clean the dataset (fill or drop missing values)
data = data.dropna()  # Alternatively, use data.fillna(value)
print("\nDataset after cleaning:\n", data.head())