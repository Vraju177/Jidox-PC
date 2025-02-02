import pandas as pd
from django.core.management.base import BaseCommand
from users.models import InventoryModel
import uuid
from datetime import datetime

class Command(BaseCommand):
    help = "Upload inventory data from a CSV file to the database."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the inventory CSV file.")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Load CSV
        self.stdout.write(f"Reading data from {csv_file}...")
        df = pd.read_csv(csv_file)

        # Ensure all required fields are present
        required_fields = [
            'id', 'manufacturer', 'product_item', 'description', 'total_ins', 
            'total_outs', 'date_out', 'stock_inhand', 'sr_no', 'mac_product_no',
            'to_user', 'to_client', 'ticket_id', 'inventory_comments', 'created_date'
        ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            self.stderr.write(f"Missing fields in CSV: {', '.join(missing_fields)}")
            return

        # Convert numeric fields to the appropriate data type
        df['total_ins'] = pd.to_numeric(df['total_ins'], errors='coerce')  # Convert to number, replace errors with NaN
        df['total_outs'] = pd.to_numeric(df['total_outs'], errors='coerce')  # Same for total_outs
        df['stock_inhand'] = pd.to_numeric(df['stock_inhand'], errors='coerce')  # Convert stock_inhand

        # Handle NaN or missing values for numeric fields (replace with 0 or another default)
        df['total_ins'] = df['total_ins'].fillna(0)
        df['total_outs'] = df['total_outs'].fillna(0)
        df['stock_inhand'] = df['stock_inhand'].fillna(0)

        # Ensure that 'ticket_id' is truncated to a maximum length (e.g., 50 characters)
        max_ticket_id_length = 50  # Adjust this value if needed
        df['ticket_id'] = df['ticket_id'].str[:max_ticket_id_length]

        # Handle missing or invalid 'id' by setting a default value or using the CSV's 'id' directly
        # Explicitly handle NaN in the 'id' column by replacing them with a default value (e.g., 0)
        df['id'] = df['id'].apply(lambda x: 0 if pd.isna(x) else x)  # Replace NaN in 'id' with 0

        # Iterate and create objects, directly accepting all rows
        inventory_objects = []
        for _, row in df.iterrows():
            inventory_objects.append(InventoryModel(
                id=int(row['id']),  # Use the id directly as per the CSV
                manufacturer=row['manufacturer'],
                product_item=row['product_item'],
                description=row['description'],
                total_ins=int(row['total_ins']),  # Ensure total_ins is an integer
                total_outs=int(row['total_outs']),  # Ensure total_outs is an integer
                date_out=row['date_out'] if pd.notna(row['date_out']) else None,
                stock_inhand=int(row['stock_inhand']),  # Ensure stock_inhand is an integer
                sr_no=row['sr_no'],
                mac_product_no=row['mac_product_no'],
                to_user=row['to_user'],
                to_client=row['to_client'],
                ticket_id=row['ticket_id'],  # Truncated to the maximum length
                inventory_comments=row['inventory_comments'],
                created_date=row['created_date'] if pd.notna(row['created_date']) else None
            ))

        # Bulk create
        self.stdout.write("Uploading data...")
        try:
            InventoryModel.objects.bulk_create(inventory_objects)
            self.stdout.write(self.style.SUCCESS("Inventory data uploaded successfully!"))
        except Exception as e:
            self.stderr.write(f"Error occurred while uploading data: {e}")
