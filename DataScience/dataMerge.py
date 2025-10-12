import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# address dictionary with names as keys & addresses as values
address = {'Pandas': 'NewYork', 'Geeks': 'Chicago',
            'for': 'Boston', 'Geeks_2': 'Miami'}

# Add the 'Address' column by mapping the 'Name' column
# to the address dictionary
df['Address'] = df['Name'].map(address)

print(df)

#merge two dataframes: one with student names and another with their scores using the name column


# Create the first DataFrame with student names
df_names = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'student_id': [101, 102, 103, 104]
})

# Create the second DataFrame with student scores
df_scores = pd.DataFrame({
    'name': ['Bob', 'Alice', 'Eve', 'Charlie'],
    'score': [85, 92, 78, 95]
})

# Merge the two DataFrames on the 'name' column
# An inner join is the default, keeping only rows where 'name' exists in both DataFrames.
merged_df = pd.merge(df_names, df_scores, on='name')

print(merged_df)