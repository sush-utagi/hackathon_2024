import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
file_path = 'B4_truck_movements_01.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Calculate angles between consecutive points
angles = []
for i in range(1, len(data) - 1):
    x1, y1 = data['X'].iloc[i-1], data['Y'].iloc[i-1]
    x2, y2 = data['X'].iloc[i], data['Y'].iloc[i]
    x3, y3 = data['X'].iloc[i+1], data['Y'].iloc[i+1]

    # Vectors AB and BC
    AB = np.array([x2 - x1, y2 - y1])
    BC = np.array([x3 - x2, y3 - y2])

    # Calculate angle using dot product
    angle_rad = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))
    angle_deg = np.degrees(angle_rad)

    angles.append(angle_deg)

# Plot the trajectory and angles
plt.figure(figsize=(12, 8))

# Plot trajectory
plt.plot(data['X'], data['Y'], marker='o', linestyle='-', color='b', label='Trajectory')

# Plot angles
scaled_angles = [a * 0.01 for a in angles]  # Scale angles for visibility
plt.scatter(data['X'].iloc[1:-1], data['Y'].iloc[1:-1], s=100, c=scaled_angles, cmap='viridis', marker='o', edgecolor='black', zorder=3, label='Steering Angle')

# Add colorbar for angles
plt.colorbar(label='Steering Angle (degrees)')

plt.title('Truck Movements and Steering Angles')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
