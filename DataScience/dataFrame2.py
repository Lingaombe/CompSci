import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'Salary': [50000.0, 60000.50, 45000.0],
        'IsEmployed': [True, False, True]}
df = pd.DataFrame(data)

# Print the data types of each column
print(df.dtypes)

# Get summary statistics for numerical columns
summary_statistics = df.describe()

print(summary_statistics)

#select only the name and age columns from the dataframe.

selected_columns_df = df[['Name', 'Age']]

# Print the new DataFrame with selected columns
print(selected_columns_df)

# display the details of the third row using .iloc.
# The index for the third row is 2 (0-indexed)
third_row = df.iloc[2]

print("Details of the third row:")
print(third_row)

# filter and display all rows where age > 25

filtered_df = df[df['Age'] > 25]

# Display the filtered DataFrame
print(filtered_df)

