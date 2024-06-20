import matplotlib.pyplot as plt
import pandas as pd

# Read the specific sheet and columns from the first Excel file
df1 = pd.read_excel('hanoi_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'co'])
# Read the specific sheet and columns from the second Excel file
df2 = pd.read_excel('hcm_air_pollution_data_monthly.xlsx', sheet_name='Sheet1', usecols=['Month', 'co'])

# Convert the 'Month' and 'co' columns of the DataFrames to lists
months1 = df1['Month'].tolist()
co_values1 = df1['co'].tolist()
months2 = df2['Month'].tolist()
co_values2 = df2['co'].tolist()

# Plotting the data from the first file
plt.plot(months1, co_values1, label='Hanoi', color='blue')

# Plotting the data from the second file
plt.plot(months2, co_values2, label='HCM', color='red')

# Naming the x axis
plt.xlabel('Month')
# Naming the y axis
plt.ylabel('CO Levels')

# Giving a title to the graph
plt.title('CO Levels Comparison between Hanoi and HCM')

# Adding a legend to distinguish between the two lines
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Function to show the plot
plt.show()
