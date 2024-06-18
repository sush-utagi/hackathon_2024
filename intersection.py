import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the data from the CSV files
road_data_file = 'Data/B4_road_coordinates.csv'
intersections_data_file = 'Data/B4_intersections.csv'

# road_df = pd.read_csv(road_data_file)

# Function to convert coordinates to a format suitable for plotting (latitude and longitude)
def convert_coords(x, y):
    return y / 1e6, x / 1e6

# Convert the coordinates for roads
# road_df['lat'], road_df['lon'] = zip(*road_df.apply(lambda row: convert_coords(row['x'], row['y']), axis=1))

# Load and parse the intersections data
def parse_intersections(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'([^,]+),"LINESTRING\(([^)]+)\)"', line)
            # if(line[4] != '0'): continue
            if match and line[0:6] == "INT_01":
                intersection_id = match.group(1)
                coordinates = match.group(2)
                coord_list = coordinates.split(',')
                if coord_list[0] == coord_list[-1]:
                    for coord in coord_list:
                        lon, lat = map(float, coord.split())
                        data.append((intersection_id, lat, lon, 'box'))
                elif len(coord_list) == 2:
                    for coord in coord_list:
                        lon, lat = map(float, coord.split())
                        data.append((intersection_id, lat, lon, 'special'))
                else:  
                    for coord in coord_list:
                        lon, lat = map(float, coord.split())
                        data.append((intersection_id, lat, lon, 'route'))
    return pd.DataFrame(data, columns=['IntersectionID', 'lat', 'lon', 'type'])

intersections_df = parse_intersections(intersections_data_file)

# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))  # Increase the figure size for higher resolution

# Plot the road coordinates
# ax.scatter(road_df['lon']+ 100, road_df['lat']-20, c='blue', marker='o', label='Road Points')

# for (intersection_id, type_), group in intersections_df.groupby(['IntersectionID', 'type']):
#     group = group.sort_values(by=['lat', 'lon'])
#     latitudes = group['lat'].values
#     longitudes = group['lon'].values

#     label = f'Intersection {intersection_id} ({type_})'
#     ax.plot(longitudes, latitudes, marker='o', linestyle='-', label=label)


# Plot the intersections coordinates
# for intersection_id, group in intersections_df.groupby('IntersectionID'):
box = []
routes = []
first = True
for type_, group in intersections_df.groupby('type'):
    if type_ == 'box':
        color = 'red'
    else:
        if first:
            first = False
            color = 'green'
        color = 'blue'
    # if type_ == 'special':
    #     color = 'green'
    for intersection_id, subgroup in group.groupby('IntersectionID'):
        ax.plot(subgroup['lon'], subgroup['lat'], marker='o', linestyle='-', color=color, label=f'Intersection {intersection_id} ({type_})')
    # ax.plot(group['lon'], group['lat'], marker='o', linestyle='-', label=f'Intersection {intersection_id}')







# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
# ax.set_title('Road Coordinates and Intersections Visualization')
ax.set_title('Intersections Visualization')

ax.legend()

# Show the plot
plt.grid(True)
plt.show()