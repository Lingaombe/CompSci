#change all values in the city column to uppercase.
import pandas as pd

data = {'city': ['london', 'paris', 'new york'],
        'population': [8982000, 2141000, 8419000]}
df = pd.DataFrame(data)

# Convert values in the 'city' column to uppercase
df['city'] = df['city'].str.upper()

# Display the updated DataFrame
print(df)

#group the data by city and calculate the average age for each city

data = {'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York'],
        'Age': [25, 30, 22, 28, 35, 21]}
df = pd.DataFrame(data)
average_age_by_city = df.groupby('City')['Age'].mean()
print(average_age_by_city)

#count the number of people in each city

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'city': ['New York', 'London', 'New York', 'Paris', 'London', 'New York']}
df = pd.DataFrame(data)

# Group by 'city' and count the size of each group
city_counts = df.groupby('city').size().reset_index(name='Number of People')
print(city_counts)

#sort the dataframe by the age column in descending order.

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 35],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Sort the DataFrame by 'Age' in descending order
df_sorted = df.sort_values(by='Age', ascending=False)

# Print the sorted DataFrame
print(df_sorted)

#rank people based on their salary from highest to lowest

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [75000, 90000, 60000, 90000, 80000]}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Salary', ascending=False)
df_sorted['Rank'] = df_sorted['Salary'].rank(method='dense', ascending=False)
    # Convert rank to integer if desired
df_sorted['Rank'] = df_sorted['Rank'].astype(int)
print(df_sorted)