# Import necessary libraries
from datetime import datetime
import pandas as pd
from meteostat import Point, Daily
import os

# Set time period
start = datetime(2018, 1, 1)
end = datetime(2023, 12, 31)

location = Point(21.0245, 105.8412)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

# Convert fetched data to pandas DataFrame
df = data.interpolate()  # Interpolate missing values if any

# Format index as dd-mm-yyyy
df.index = df.index.strftime('%d-%m-%Y')

# Insert the date column as the first column
df.insert(0, 'date', df.index)

# Export data to Excel
excel_file = 'weather_data_hanoi.xlsx'

# Delete the file if it exists
if os.path.exists(excel_file):
    os.remove(excel_file)
    print(f"Old {excel_file} deleted.")
    
df.to_excel(excel_file, index=False)

print(f"Data has been exported to {excel_file}")
print(data)
