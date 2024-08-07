# Import the Data from data.py
from data_NN import Data

# Convert list of tuples to DataFrame for easier manipulation
import pandas as pd

# Convert Data to a DataFrame
df = pd.DataFrame(Data, columns=['Theoretical%', 'Result'])

# Calculate the count of 'Loose' and 'Won' matches for each theoretical percentage
grouped = df.groupby('Theoretical%')['Result'].value_counts().unstack().fillna(0)

# Calculate the percentage of wins (%OF WIN)
grouped['%OF WIN'] = grouped['Won'] / (grouped['Loose'] + grouped['Won']) * 100

# Round the number of 'Loose' and 'Won' to integers
grouped['Loose'] = grouped['Loose'].astype(int)
grouped['Won'] = grouped['Won'].astype(int)

# Round %OF WIN to one decimal place
grouped['%OF WIN'] = grouped['%OF WIN'].round(1)

# Rename columns for clarity
grouped.columns.name = None

# Save the result to a CSV file
output_file = 'result_NN.csv'
grouped.to_csv(output_file)

print(f"Data saved to {output_file}")
