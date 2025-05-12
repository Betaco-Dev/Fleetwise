from django.db import models
import json
import pickle

class AnalyticsReport(models.Model):
    report_name = models.CharField(max_length=100)
    created_date = models.DateField()
    data = models.BinaryField()

    def __str__(self):
        return self.report_name

    def deserialize_json_data(self):
        """
        Deserialize the binary data as JSON.
        Returns a Python dictionary or list.
        """
        try:
            return json.loads(self.data.decode('utf-8'))
        except (ValueError, TypeError, UnicodeDecodeError) as e:
            raise ValueError(f"Failed to deserialize JSON data: {e}")

    def deserialize_pickle_data(self):
        """
        Deserialize the binary data as a Python object (using pickle).
        Returns any Python object serialized with pickle.
        """
        try:
            return pickle.loads(self.data)
        except (pickle.PickleError, ValueError) as e:
            raise ValueError(f"Failed to deserialize pickle data: {e}")

    def save_data_to_file(self, file_path):
        """
        Save the binary data to a file at the specified path.
        """
        try:
            with open(file_path, 'wb') as file:
                file.write(self.data)
        except IOError as e:
            raise ValueError(f"Failed to save data to file: {e}")
