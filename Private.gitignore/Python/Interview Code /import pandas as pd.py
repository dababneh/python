import pandas as pd

# Load the CSV file
mock_data = pd.read_csv('mock_temperature_data.csv')

# Convert the 'datetime' column to pandas datetime type
mock_data['datetime'] = pd.to_datetime(mock_data['datetime'])

# Extract the date (without time) for grouping by day
mock_data['date'] = mock_data['datetime'].dt.date

# Group by the 'date' column and calculate min, max, and average temperatures for each day
daily_stats = mock_data.groupby('date').agg(
    min_temp=('temperature', 'min'),
    max_temp=('temperature', 'max'),
    avg_temp=('temperature', 'mean')
).reset_index()

# Convert the result to lists of min, max, and avg temperatures
min_temps = daily_stats['min_temp'].tolist()
max_temps = daily_stats['max_temp'].tolist()
avg_temps = daily_stats['avg_temp'].tolist()

# Return or print the arrays
print("Min Temperatures:", min_temps)
print("Max Temperatures:", max_temps)
print("Avg Temperatures:", avg_temps)
