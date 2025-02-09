import pandas as pd
from django.core.management.base import BaseCommand
from users.models import InventoryModel
from datetime import datetime

class Command(BaseCommand):
    help = "Upload inventory stock received data from a CSV file to the database."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the inventory-ins CSV file.")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Load CSV
        self.stdout.write(f"Reading data from {csv_file}...")
        df = pd.read_csv(csv_file)

        # Ensure all required fields are present
        required_fields = [
            'id', 'manufacturer', 'product_item', 'description', 
            'total_stock_received', 'serial_no', 'mac_product_no', 'comments', 'stock_in_date'
        ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            self.stderr.write(f"Missing fields in CSV: {', '.join(missing_fields)}")
            return

        # Convert numeric fields to the appropriate data type
        df['total_stock_received'] = pd.to_numeric(df['total_stock_received'], errors='coerce').fillna(0).astype(int)
        df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)
        
        # Convert date field
        df['stock_in_date'] = pd.to_datetime(df['stock_in_date'], errors='coerce')

        # Iterate and create objects
        inventory_objects = []
        for _, row in df.iterrows():
            inventory_objects.append(InventoryModel(
                id=row['id'],
                manufacturer=row['manufacturer'],
                product_item=row['product_item'],
                description=row['description'],
                total_ins=row['total_stock_received'],  # Mapping CSV total_stock_received to total_ins
                sr_no=row['serial_no'],
                mac_product_no=row['mac_product_no'],
                inventory_comments=row['comments'],
                created_date=row['stock_in_date'] if pd.notna(row['stock_in_date']) else None
            ))

        # Bulk create
        self.stdout.write("Uploading data...")
        try:
            InventoryModel.objects.bulk_create(inventory_objects)
            self.stdout.write(self.style.SUCCESS("Inventory data uploaded successfully!"))
        except Exception as e:
            self.stderr.write(f"Error occurred while uploading data: {e}")
