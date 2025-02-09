import pandas as pd
from django.core.management.base import BaseCommand
from users.models import InventoryModel
from datetime import datetime

class Command(BaseCommand):
    help = "Upload inventory out data from a CSV file to the database."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the inventory-outs CSV file.")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Load CSV
        self.stdout.write(f"Reading data from {csv_file}...")
        df = pd.read_csv(csv_file)

        # Ensure all required fields are present
        required_fields = [
            'id', 'manufacturer', 'product_item', 'description', 'total_stock_sent', 
            'stock_out_date', 'serial_no', 'mac_product_no', 'to_user', 'to_client', 
            'ticket_id', 'comments', 'stock_in_date'
        ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            self.stderr.write(f"Missing fields in CSV: {', '.join(missing_fields)}")
            return

        # Convert numeric fields to the appropriate data type
        df['total_stock_sent'] = pd.to_numeric(df['total_stock_sent'], errors='coerce').fillna(0).astype(int)
        df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)

        # Convert date fields to proper datetime format
        df['stock_out_date'] = pd.to_datetime(df['stock_out_date'], errors='coerce')
        df['stock_in_date'] = pd.to_datetime(df['stock_in_date'], errors='coerce')

        # Ensure that 'ticket_id' is truncated to a maximum length (e.g., 50 characters)
        max_ticket_id_length = 50
        df['ticket_id'] = df['ticket_id'].astype(str).str[:max_ticket_id_length]

        # Iterate and create objects, directly accepting all rows
        inventory_objects = []
        for _, row in df.iterrows():
            inventory_objects.append(InventoryModel(
                id=row['id'],
                manufacturer=row['manufacturer'],
                product_item=row['product_item'],
                description=row['description'],
                total_outs=row['total_stock_sent'],  # Mapped to total_outs
                date_out=row['stock_out_date'],
                sr_no=row['serial_no'],
                mac_product_no=row['mac_product_no'],
                to_user=row['to_user'],
                to_client=row['to_client'],
                ticket_id=row['ticket_id'],
                inventory_comments=row['comments'],
                created_date=row['stock_in_date']
            ))

        # Bulk create
        self.stdout.write("Uploading data...")
        try:
            InventoryModel.objects.bulk_create(inventory_objects)
            self.stdout.write(self.style.SUCCESS("Inventory out data uploaded successfully!"))
        except Exception as e:
            self.stderr.write(f"Error occurred while uploading data: {e}")
