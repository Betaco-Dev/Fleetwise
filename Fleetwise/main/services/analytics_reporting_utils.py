import json
import pickle
import csv
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from Fleetwise.models import AnalyticsReport

class AnalyticsReportService:
    @staticmethod
    def create_report(report_name, created_date, data):
        """Create a new AnalyticsReport entry."""
        try:
            report = AnalyticsReport.objects.create(
                report_name=report_name,
                created_date=created_date,
                data=data
            )
            return report
        except Exception as e:
            raise ValueError(f"Failed to create report: {e}")

    @staticmethod
    def get_report_by_id(report_id):
        """Fetch a report by ID."""
        try:
            return AnalyticsReport.objects.get(id=report_id)
        except ObjectDoesNotExist:
            raise ValueError("Report not found.")
        except Exception as e:
            raise ValueError(f"Error fetching report: {e}")

    @staticmethod
    def update_report_data(report_id, new_data):
        """Update the binary data of an existing report."""
        try:
            report = AnalyticsReport.objects.get(id=report_id)
            report.data = new_data
            report.save()
            return report
        except ObjectDoesNotExist:
            raise ValueError("Report not found.")
        except Exception as e:
            raise ValueError(f"Error updating report data: {e}")

    @staticmethod
    def delete_report(report_id):
        """Delete a report by ID."""
        try:
            report = AnalyticsReport.objects.get(id=report_id)
            report.delete()
            return True
        except ObjectDoesNotExist:
            raise ValueError("Report not found.")
        except Exception as e:
            raise ValueError(f"Error deleting report: {e}")

    @staticmethod
    def filter_reports_by_date(start_date, end_date):
        """Retrieve reports within a date range."""
        try:
            return AnalyticsReport.objects.filter(created_date__range=(start_date, end_date))
        except Exception as e:
            raise ValueError(f"Error filtering reports by date: {e}")

    @staticmethod
    def export_reports_to_csv(file_path):
        """Export all reports to a CSV file."""
        try:
            reports = AnalyticsReport.objects.all()
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Report Name', 'Created Date'])
                for report in reports:
                    writer.writerow([report.id, report.report_name, report.created_date])
            return file_path
        except Exception as e:
            raise ValueError(f"Failed to export reports: {e}")

    @staticmethod
    def deserialize_json(report):
        """Deserialize JSON data from a report instance."""
        try:
            return json.loads(report.data.decode('utf-8'))
        except (ValueError, TypeError, UnicodeDecodeError) as e:
            raise ValueError(f"Failed to deserialize JSON data: {e}")

    @staticmethod
    def deserialize_pickle(report):
        """Deserialize pickle data from a report instance."""
        try:
            return pickle.loads(report.data)
        except (pickle.PickleError, ValueError) as e:
            raise ValueError(f"Failed to deserialize pickle data: {e}")
