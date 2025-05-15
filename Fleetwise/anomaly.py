from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Example GPS data (latitude, longitude)
gps_data = np.array([
    [37.7749, -122.4194],
    [37.7750, -122.4195],
    [37.7748, -122.4193],
    [0.0, 0.0],  # Anomalous GPS point
])

# Scale the data
scaler = StandardScaler()
gps_data_scaled = scaler.fit_transform(gps_data)

# Train IsolationForest model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(gps_data_scaled)
anomalies = model.predict(gps_data_scaled)

# Print anomalies
for i, (point, label) in enumerate(zip(gps_data, anomalies)):
    status = "Anomaly" if label == -1 else "Normal"
    print(f"Point {i}: {point} - {status}")

# Visualize the data
plt.figure(figsize=(8, 6))
for i, (point, label) in enumerate(zip(gps_data, anomalies)):
    color = 'red' if label == -1 else 'blue'
    plt.scatter(point[0], point[1], color=color, label="Anomaly" if label == -1 else "Normal")
plt.title("GPS Data Anomaly Detection")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend(["Normal", "Anomaly"])
plt.show()
