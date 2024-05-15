import pandas as pd

# Load the CSV file
df = pd.read_csv('file.csv')

# Remove rows where a specific column says "Airbnb.com"
df = df[df['Column Name'] != 'Airbnb.com']

# Convert the date column to datetime type
df['Arrival Date'] = pd.to_datetime(df['Arrival Date'])

# Remove records where the arrival date is in a previous quarter
current_quarter = pd.Timestamp.now().quarter
df = df[df['Arrival Date'].dt.quarter == current_quarter]

# Replace commas with semicolons as separators
df = df.replace(',', ';', regex=True)

# Save the modified file
df.to_csv('modified_file.csv', index=False)
