import pandas as pd
import utm

# Function to convert UTM coordinates to latitude and longitude
def convert_utm_to_latlon(easting, northing, zone_number=50, zone_letter='S'):
    lat, lon = utm.to_latlon(easting, northing, zone_number, zone_letter)
    return lat, lon

# Read the data from the CSV file
file_path = 'Data/B4_Truck_movements.csv'  # Adjust the path as necessary
df = pd.read_csv(file_path)

# Convert the UTM coordinates to latitude and longitude
df['Latitude'], df['Longitude'] = zip(*df.apply(lambda row: convert_utm_to_latlon(row['X'], row['Y']), axis=1))

# Select relevant columns and rename for clarity
df = df[['Truck', 'TimeStamp', 'Longitude', 'Latitude']]

# Write the new data to a new CSV file
output_file_path = 'Data/trucks.csv'  # Adjust the path as necessary
df.to_csv(output_file_path, index=False)

print(f"Converted coordinates have been written to {output_file_path}")
