import pandas as pd
import matplotlib.pyplot as plt
import random

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Read the data from the CSV file
file_path = '/mnt/Data/B4_road_coordinates.csv'  # Adjust the path as necessary
df = pd.read_csv(file_path)

# Create the plot
plt.figure(figsize=(10, 6))

# Group by area Id and plot each group with a different color
for area_id, group in df.groupby('area Id'):
    lons = group['x'].values
    lats = group['y'].values
    color = random_color()
    plt.plot(lons, lats, marker='o', linestyle='-', color=color, label=f'Area ID {area_id}')

# Add labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Plot of Road Coordinates by Area ID')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
