import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Sample data
data = {
    "vehicle_id": [1, 2, 3],
    "last_maintenance_date": ["2025-01-01", "2025-02-01", "2025-03-01"],
    "mileage": [12000, 15000, 10000],
}
df = pd.DataFrame(data)
df['last_maintenance_date'] = pd.to_datetime(df['last_maintenance_date'])

# Train AI model
X = df[['mileage']]
y = (df['last_maintenance_date'] + pd.to_timedelta(180, unit='d')).astype(int)  # Predict next maintenance in 180 days
model = LinearRegression()
model.fit(X, y)

# Predict for a new vehicle
new_vehicle = {"mileage": 14000}
predicted_date = model.predict(pd.DataFrame([new_vehicle]))
predicted_date = datetime.fromtimestamp(predicted_date[0] / 1e9)  # Convert to datetime
print(f"Predicted Maintenance Date: {predicted_date}")
