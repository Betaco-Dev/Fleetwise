import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

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
        df = pd.DataFrame(self.training_data)
        df['last_maintenance_date'] = pd.to_datetime(df['last_maintenance_date'])
        X = df[['mileage']]
        y = (df['last_maintenance_date'] + pd.to_timedelta(180, unit='d')).view('int64')
        self.model = LinearRegression()
        self.model.fit(X, y)
        print("Maintenance prediction model trained.")

    def predict_next_maintenance(self, mileage):
        if not self.model:
            raise ValueError("Model is not trained. Call `train_maintenance_model` first.")
        predicted_date = self.model.predict([[mileage]])[0]
        return datetime.fromtimestamp(predicted_date / 1e9)
