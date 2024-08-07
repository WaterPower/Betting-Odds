import pandas as pd

# Load Excel file
filename = 'matches_data.csv'  # Replace with your actual file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different

# Read Excel sheet into a DataFrame without headers
df = pd.read_excel(filename, sheet_name=sheet_name, header=None)

Data = []

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    implied_proba = row[0]   # Accessing the first column (0-based index)
    result = row[1]      # Accessing the second column (0-based index)
    Data.append((implied_proba, result))  # Append tuple (player_id, result) to Data list

# Write the Data list to a Python file
output_file = 'data22.py'

with open(output_file, 'w') as f:
    f.write('Data = [\n')
    for implied_proba, result in Data:
        f.write(f'    ({implied_proba}, "{result}"),\n')
    f.write(']\n')

print(f"Data written to '{output_file}'")