import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'Data/trucks.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)

# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))  # Increase the figure size for higher resolution

# Plot the data for each truck with a different color
truck_ids = data['Truck'].unique()
colors = plt.cm.get_cmap('tab10', len(truck_ids))

for i, truck_id in enumerate(truck_ids):
    truck_data = data[data['Truck'] == truck_id]
    ax.plot(truck_data['Longitude'], truck_data['Latitude'], marker='o', linestyle='-', color=colors(i), label=f'Truck {truck_id}')

# Add labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Truck Movements')
ax.legend()

# Show the plot
plt.grid(True)
plt.show()
