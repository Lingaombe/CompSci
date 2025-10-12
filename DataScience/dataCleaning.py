#data cleaning
# replace all mising (NAN) values with 0.

import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, np.nan, 35, 40],
        'City': ['New York', 'San Francisco', np.nan, 'London'],
        'Salary': [50000, 60000, 55000, 62000]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace all NaN values with 0
df_filled = df.fillna(0)

print("\nDataFrame after replacing NaN with 0:")
print(df_filled)

#drop all rows where the city columns has missing values.

print("Original DataFrame:")
print(df)

# Drop rows where the 'City' column has missing values
df_cleaned = df.dropna(subset=['City'])

print("\nDataFrame after dropping rows with missing 'City' values:")
print(df_cleaned)

#convert a column named date to datetime format

# Assuming df is your DataFrame and 'date' is the column to convert

data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'value': [10, 20, 30]}
df = pd.DataFrame(data)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Verify the data type
print(df.dtypes)

