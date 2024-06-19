# importing the required module
import matplotlib.pyplot as plt
import pandas as pd
 
 # Example: Read specific sheet and columns
df = pd.read_excel('hanoi_air_pollution_data.xlsx', sheet_name='Sheet1', usecols=['no'])

# Convert the 'AQI' column of the DataFrame to a list
aqi_values = df['no'].tolist()

# Get the number of rows in the DataFrame
num_rows = df.shape[0]

# Generate a list of numbers from 1 to num_rows
counted_list = list(range(1, num_rows + 1))

# x axis values
x = counted_list
# corresponding y axis values
y = aqi_values
 
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('no')
 
# giving a title to my graph
plt.title('no Graph')
 
# function to show the plot
plt.show()