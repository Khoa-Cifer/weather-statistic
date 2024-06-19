import requests
from datetime import datetime
import pandas as pd
import os

lat = 21.0245
lon = 105.8412
APIkey = '7a11d0dc5b39eccc81c453338085c028'  # Replace with your actual OpenWeatherMap API key

# Define start and end dates (as Unix timestamps)
start_date = datetime(2018, 1, 1).timestamp()  
end_date = datetime(2023, 12, 31).timestamp()

# Construct the API URL with parameters
apiKey = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={int(start_date)}&end={int(end_date)}&appid={APIkey}'

# Make the API request
response = requests.get(apiKey)

data = response.json()

# Prepare to store daily averages
daily_averages = {
    'Date': [],
    'AQI': [],
    'co': [],
    'no': [],
    'no2': [],
    'o3': [],
    'so2': [],
    'pm2_5': [],
    'pm10': [],
    'nh3': []
}

# Aggregate data into daily averages
for entry in data['list']:
    dt = datetime.utcfromtimestamp(entry['dt'])
    date_key = dt.strftime('%Y-%m-%d')

    if date_key not in daily_averages['Date']:
        daily_averages['Date'].append(date_key)
        for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
            daily_averages[component].append(entry['components'][component])
        daily_averages['AQI'].append(entry['main']['aqi'])   
    else:
        for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
            daily_averages[component][-1] += entry['components'][component]

# Calculate daily averages
for i in range(len(daily_averages['Date'])):
    for component in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
        daily_averages[component][i] /= 24  # Assuming hourly data, divide by 24 to get daily average

# Create DataFrame from daily averages
df = pd.DataFrame(daily_averages)

# Export data to Excel
excel_file = 'hanoi_air_pollution_data.xlsx'
# Delete the file if it exists
if os.path.exists(excel_file):
    os.remove(excel_file)
    print(f"Old {excel_file} deleted.")
    
df.to_excel(excel_file, index=False)

print(f"Data has been exported to {excel_file}")