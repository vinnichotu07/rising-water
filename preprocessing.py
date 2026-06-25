import pandas as pd

# Load data
data = pd.read_csv('rising_waters_data.csv')

# Check missing values
print("Missing values:")
print(data.isnull().sum())

# Fill missing values
data.fillna(data.mean(numeric_only=True), inplace=True)

# Remove duplicates
data = data.drop_duplicates()

# Save clean data
data.to_csv('clean_data.csv', index=False)

print("Data cleaning DONE!")
print(data.head())