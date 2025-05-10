from sklearn.ensemble import IsolationForest
import numpy as np

# Example GPS data (latitude, longitude)
gps_data = np.array([
    [37.7749, -122.4194],
    [37.7750, -122.4195],
    [37.7748, -122.4193],
    [0.0, 0.0],  # Anomalous GPS point
])
model = IsolationForest(contamination=0.1)
model.fit(gps_data)
anomalies = model.predict(gps_data)
print("Anomalies:", anomalies)  # -1 indicates anomaly
