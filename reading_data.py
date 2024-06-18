import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import matplotlib.colors as mcolors

# Load and parse the intersections data
def parse_intersections(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'([^,]+),"LINESTRING\(([^)]+)\)"', line)
            if match:
                intersection_id = match.group(1)
                coordinates = match.group(2)
                coord_list = coordinates.split(',')
                for coord in coord_list:
                    lon, lat = map(float, coord.split())
                    data.append((intersection_id, lat, lon))
    return pd.DataFrame(data, columns=['IntersectionID', 'lat', 'lon'])

# Load the intersections data file
intersections_data_file = 'Data/B4_intersections.csv'
intersections_df = parse_intersections(intersections_data_file)

# Get a list of unique intersection IDs
intersection_ids = intersections_df['IntersectionID'].unique()

# Create a color map
colors = list(mcolors.TABLEAU_COLORS.keys())
color_map = {intersection_id: colors[i % len(colors)] for i, intersection_id in enumerate(intersection_ids)}

# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the intersections coordinates
for intersection_id, group in intersections_df.groupby('IntersectionID'):
    color = color_map[intersection_id]
    ax.plot(group['lon'], group['lat'], marker='o', linestyle='-', color=color, label=f'Intersection {intersection_id}')

# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Intersections Visualization')
ax.legend()

# Show the plot
plt.grid(True)
plt.show()
