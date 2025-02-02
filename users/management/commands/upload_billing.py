import pandas as pd
from django.core.management.base import BaseCommand
from users.models import BillingModel
import uuid

class Command(BaseCommand):
    help = "Upload billing data from a CSV file to the database."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the billing CSV file.")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Load CSV
        self.stdout.write(f"Reading data from {csv_file}...")
        df = pd.read_csv(csv_file)

        # Ensure all required fields are present
        required_fields = [
            'id', 'client_name', 'client_address', 'billing_to', 'service_type',
            'bill_description', 'ticket_id', 'billing_date', 'emailed',
            'comments', 'invoice_no', 'invoice_date'
        ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            self.stderr.write(f"Missing fields in CSV: {', '.join(missing_fields)}")
            return

        # Convert "Yes"/"No" to True/False, and handle NaN values (defaulting to False)
        df['emailed'] = df['emailed'].map({'Yes': True, 'No': False})
        df['emailed'] = df['emailed'].fillna(False)

        # Handle missing or invalid invoice_no (assign a UUID or fallback value)
        df['invoice_no'] = df['invoice_no'].apply(lambda x: str(uuid.uuid4()) if pd.isna(x) else x)

        # Truncate the invoice_no to the max length allowed (e.g., 50 characters)
        max_invoice_length = 50
        df['invoice_no'] = df['invoice_no'].str[:max_invoice_length]

        # Truncate the ticket_id to the max length allowed (e.g., 50 characters)
        max_ticket_id_length = 50  # You can update this with the actual maximum length of ticket_id
        df['ticket_id'] = df['ticket_id'].str[:max_ticket_id_length]

        # Iterate and create objects
        billing_objects = []
        for _, row in df.iterrows():
            billing_objects.append(BillingModel(
                client_name=row['client_name'],
                client_address=row['client_address'],
                billing_to=row['billing_to'],
                service_type=row['service_type'],
                bill_description=row['bill_description'],
                ticket_id=row['ticket_id'],  # Truncated to the maximum length
                billing_date=row['billing_date'],
                emailed=row['emailed'],  # Already cleaned up here
                comments=row['comments'],
                invoice_no=row['invoice_no'],  # Truncated to the maximum length
                invoice_date=row['invoice_date'] if pd.notna(row['invoice_date']) else None
            ))

        # Bulk create
        self.stdout.write("Uploading data...")
        BillingModel.objects.bulk_create(billing_objects)

        self.stdout.write(self.style.SUCCESS("Billing data uploaded successfully!"))
