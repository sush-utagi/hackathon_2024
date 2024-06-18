import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# Function to calculate the distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to find the closest points
def find_closest_points(route_points, box_points, num_points=4):
    closest_points = []
    for box_point in box_points:
        distances = [calculate_distance(box_point, route_point) for route_point in route_points]
        closest_point_idx = np.argmin(distances)
        closest_points.append(route_points[closest_point_idx])
        route_points = np.delete(route_points, closest_point_idx, axis=0)
    return closest_points

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
                    data.append((intersection_id, lat, lon, 'route' if len(coord_list) > 2 else 'box'))
    return pd.DataFrame(data, columns=['IntersectionID', 'lat', 'lon', 'type'])

# Load the intersections data file
intersections_data_file = 'Data/B4_intersections.csv'
intersections_df = parse_intersections(intersections_data_file)

# Separate the data into bounding box and route points
box_points = intersections_df[intersections_df['type'] == 'box'][['lat', 'lon']].to_numpy()
route_points = intersections_df[intersections_df['type'] == 'route'][['lat', 'lon']].to_numpy()

# Find the closest points
closest_points = find_closest_points(route_points, box_points)
closest_points = np.array(closest_points)  # Ensure closest_points is a 2D array

# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the intersections coordinates
for type_, group in intersections_df.groupby('type'):
    color = 'red' if type_ == 'box' else 'blue'
    ax.plot(group['lon'], group['lat'], marker='o', linestyle='-', color=color, label=f'Intersection INT_01 ({type_})')

# Highlight the closest points in green
if closest_points.ndim == 2:  # Check if closest_points is a 2D array
    ax.scatter(closest_points[:, 1], closest_points[:, 0], color='green', s=100, zorder=5)

# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Intersections Visualization')
ax.legend()

# Show the plot
plt.grid(True)
plt.show()
