import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
import numpy as np

# Maintenance Prediction Service
class MaintenancePredictionService:
    def __init__(self):
        # Example of predefined training data
        self.training_data = {
            "vehicle_id": [1, 2, 3],
            "last_maintenance_date": ["2025-01-01", "2025-02-01", "2025-03-01"],
            "mileage": [12000, 15000, 10000],
        }
        self.model = None

  def train_maintenance_model(self):
    # Create DataFrame and preprocess
    df = pd.DataFrame(self.training_data)
    df['last_maintenance_date'] = pd.to_datetime(df['last_maintenance_date'])
    
    # Predict next maintenance after 180 days (example logic)
    X = df[['mileage']]
    y = (df['last_maintenance_date'] + pd.to_timedelta(180, unit='d')).view('int64')  # nanoseconds since epoch
    
    # Train the model
    self.model = LinearRegression()
    self.model.fit(X, y)
    print("Maintenance prediction model trained.")

    def predict_next_maintenance(self, mileage):
        if not self.model:
            raise ValueError("Model is not trained. Call `train_maintenance_model` first.")
        
        # Predict the next maintenance date
        predicted_date = self.model.predict([[mileage]])[0]
        return datetime.fromtimestamp(predicted_date / 1e9)  # Convert back to datetime


# Anomaly Detection Service
class AnomalyDetectionService:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)  # Example contamination level

    def train_anomaly_model(self, data):
        # Train the model on provided data
        self.model.fit(data)
        print("Anomaly detection model trained.")

    def detect_anomalies(self, data):
        if not self.model:
            raise ValueError("Model is not trained. Call `train_anomaly_model` first.")
        
        # Predict anomalies (-1 indicates anomaly)
        predictions = self.model.predict(data)
        anomalies = [i for i, pred in enumerate(predictions) if pred == -1]
        return anomalies


# Example Usage
if __name__ == "__main__":
    # Maintenance Prediction Example
    maintenance_service = MaintenancePredictionService()
    maintenance_service.train_maintenance_model()
    next_maintenance = maintenance_service.predict_next_maintenance(mileage=14000)
    print(f"Predicted Next Maintenance Date: {next_maintenance}")

    # Anomaly Detection Example
    anomaly_service = AnomalyDetectionService()
    gps_data = np.array([
        [37.7749, -122.4194],  # Normal point
        [37.7750, -122.4195],  # Normal point
        [0.0, 0.0],            # Anomalous point
    ])
    anomaly_service.train_anomaly_model(data=gps_data)
    anomalies = anomaly_service.detect_anomalies(data=gps_data)
    print(f"Anomalous Data Indices: {anomalies}")
