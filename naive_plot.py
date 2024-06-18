import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_file = 'Data/B4_road_coordinates.csv'
df = pd.read_csv(data_file)

# Define a function to convert coordinates to a format suitable for plotting (latitude and longitude)
def convert_coords(x, y):
    # Assuming the coordinates need to be converted from some projection to WGS 84 (latitude and longitude)
    # For demonstration, let's assume they are already in WGS 84, so no conversion is needed
    # If conversion is needed, you would use a library like pyproj to transform the coordinates
    return y / 1e6, x / 1e6

# Convert the coordinates
df['lat'], df['lon'] = zip(*df.apply(lambda row: convert_coords(row['x'], row['y']), axis=1))

# Create a plot
plt.figure(figsize=(10, 8))
plt.scatter(df['lon'], df['lat'], c='blue', marker='o', label='Road Points')

# Annotate the from_loc and to_loc points
for idx, row in df.iterrows():
    plt.annotate(f"{row['from_loc']} to {row['to_loc']}", (row['lon'], row['lat']), textcoords="offset points", xytext=(0,10), ha='center')

# Add labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Road Coordinates Visualization')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
