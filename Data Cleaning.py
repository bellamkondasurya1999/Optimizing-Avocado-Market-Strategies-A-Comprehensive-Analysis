import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Load your dataset
data = pd.read_csv('Augmented_avocado.csv')

# Step 1: Fill Null Values
# Replace 'ColumnName' with the name of your column. Repeat or modify as needed.
# Example: Filling numeric columns with their mean
data['NumericColumn'] = data['NumericColumn'].fillna(data['NumericColumn'].mean())

# For categorical columns, you might want to fill with the mode (most frequent value)
data['CategoricalColumn'] = data['CategoricalColumn'].fillna(data['CategoricalColumn'].mode()[0])

# Alternatively, forward fill or backward fill can be used
data = data.fillna(method='ffill')
data = data.fillna(method='bfill')

# Step 2: Drop Unnecessary Rows
# Dropping rows where any column is null
data = data.dropna()

# Or, to drop rows only if specific columns have null values:
data = data.dropna(subset=['ColumnName1', 'ColumnName2'])

# Step 3: Remove Unnecessary Columns
# Drop columns that are not relevant to your analysis
data = data.drop(columns=['UnwantedColumn'])

# Step 4: Check for Duplicates
# Remove duplicate rows to ensure accuracy
data = data.drop_duplicates()

# Step 5: Data Type Conversion
# Convert the 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])
# Convert other columns as needed

# Step 6: Handling Outliers
# Identify and handle outliers in your data. This requires specific analysis.
# Example: using IQR or Z-scores

# Step 7: Normalization/Standardization (Example using Min-Max Scaling)
# Normalize or standardize numerical features, especially for machine learning models
scaler = MinMaxScaler()
# Replace with actual numeric column names
# data[['NumericColumn1', 'NumericColumn2']] = scaler.fit_transform(data[['NumericColumn1', 'NumericColumn2']])

# Step 8: Categorical Data Encoding (Example using One-Hot Encoding)
# Convert categorical columns to a numerical format for machine learning models
# data = pd.get_dummies(data, columns=['CategoricalColumn'])

# Save the cleaned data or continue with your analysis
# data.to_csv('path_to_save_cleaned_file.csv', index=False)
