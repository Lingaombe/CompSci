# create a dataframe with 3 columns : name,age, and city with at least 5 rows of data

import pandas as pd

# Create a dictionary with data for each column
data = {
    'name': ['Anjali', 'arati', 'Charlie', 'Diya', 'tanuja'],
    'age': [25, 27, 22, 28, 30],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame to verify
print(df)

# create a dataframe from python dictionary and print the first 3 rows.

# Print the DataFrame to verify
print(df.head(3))

#data import / export
# read a csv file named students.csv and display the first 5 rows.

df = pd.DataFrame(data)

# Save it as CSV
df.to_csv('students.csv', index=False)

# Now read it
df = pd.read_csv('students.csv')
print(df.head())

# save a dataframe to an excel file named output.xlsx.

df.to_excel('output.xlsx', index=False)

# how many rows and columns in the dataset

num_rows = len(df)
num_cols = len(df.columns)
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

