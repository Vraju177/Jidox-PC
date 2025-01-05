from django.core.management.base import BaseCommand
import csv
from users.models import User  # Adjust this import based on your app structure
from datetime import datetime

class Command(BaseCommand):
    help = "Import users from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the CSV file to import.")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)

                # Debug: Print headers and first few rows
                headers = reader.fieldnames
                self.stdout.write(f"CSV Headers: {headers}")

                for i, row in enumerate(reader):
                    self.stdout.write(f"Row {i + 1}: {row}")
                    if i >= 2:  # Only print the first 3 rows
                        break

                # Reset the file cursor and process the CSV as usual
                file.seek(0)
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        user_creation_date = datetime.strptime(row['user_creation_date'], '%Y-%m-%d').date()
                        User.objects.create(
                            username=row['username'],
                            company=row.get('company', ''),
                            full_name=row.get('full_name', ''),
                            phone_number=row.get('phone_number', ''),
                            alternate_number=row.get('alternate_number', ''),
                            email=row.get('email', ''),
                            email_password=row.get('email_password', ''),
                            service_type=row.get('service_type', ''),
                            location=row.get('location', ''),
                            branch_code=row.get('branch_code', ''),
                            node=row.get('node', ''),
                            port_number=row.get('port_number', ''),
                            rdp_password=row.get('rdp_password', ''),
                            internal_ip=row.get('internal_ip', ''),
                            pb_id=row.get('pb_id', ''),
                            pb_password=row.get('pb_password', ''),
                            extension_number=row.get('extension_number', ''),
                            notes=row.get('notes', ''),
                            user_creation_date=user_creation_date,
                            status=row['status']
                        )
                        self.stdout.write(f"Successfully imported user {row['username']}")
                    except KeyError as e:
                        self.stderr.write(f"Missing column in CSV: {e}")
                    except Exception as e:
                        self.stderr.write(f"Error importing user: {e}")

        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")
        except Exception as e:
            self.stderr.write(f"An unexpected error occurred: {e}")
