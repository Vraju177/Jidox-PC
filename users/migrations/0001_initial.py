# Generated by Django 5.0.12 on 2025-02-10 00:31

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('client_address', models.TextField(blank=True, null=True, verbose_name='Client Address')),
                ('billing_to', models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing To')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Service Type')),
                ('bill_description', models.TextField(blank=True, null=True, verbose_name='Bill Description')),
                ('ticket_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ticket ID')),
                ('emailed', models.BooleanField(default=False, verbose_name='Emailed')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('billing_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('invoice_no', models.CharField(blank=True, max_length=250, null=True, verbose_name='Invoice Number')),
                ('invoice_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Billing Model',
                'verbose_name_plural': 'Billing Models',
            },
        ),
        migrations.CreateModel(
            name='InventoryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_item', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(choices=[('Stock In', 'Stock In'), ('Stock Out', 'Stock Out')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_product_no', models.CharField(blank=True, max_length=255, null=True)),
                ('received_from', models.CharField(blank=True, max_length=255, null=True)),
                ('delivered_to', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ticket_id', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Manufacturer')),
                ('product_item', models.CharField(max_length=255, verbose_name='Product Item')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('total_ins', models.PositiveIntegerField(default=0, verbose_name='Total In Stock')),
                ('total_outs', models.PositiveIntegerField(default=0, verbose_name='Total Out Stock')),
                ('date_out', models.DateField(blank=True, null=True, verbose_name='Date Out')),
                ('stock_inhand', models.PositiveIntegerField(default=0, verbose_name='Stock In Hand')),
                ('sr_no', models.CharField(max_length=255, verbose_name='Serial Number')),
                ('mac_product_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='MAC Product No')),
                ('to_user', models.CharField(blank=True, max_length=255, null=True, verbose_name='To User')),
                ('to_client', models.CharField(blank=True, max_length=255, null=True, verbose_name='To Client')),
                ('ticket_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ticket ID')),
                ('inventory_comments', models.TextField(blank=True, null=True, verbose_name='Inventory Comments')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Inventory Model',
                'verbose_name_plural': 'Inventory Models',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='StockInHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_item', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('total_stock_received', models.PositiveIntegerField(default=0)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_product_no', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('received_from', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_in_date', models.DateField()),
                ('stock_in_hand', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StockInModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('product_item', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_stock_received', models.PositiveIntegerField(default=0)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_product_no', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('stock_in_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockOutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('product_item', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_stock_sent', models.PositiveIntegerField()),
                ('stock_out_date', models.DateField(auto_now_add=True)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_product_no', models.CharField(blank=True, max_length=255, null=True)),
                ('to_user', models.CharField(blank=True, max_length=255, null=True)),
                ('to_client', models.CharField(blank=True, max_length=255, null=True)),
                ('ticket_id', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('stock_in_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name of User')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('alternate_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_password', models.CharField(blank=True, max_length=255, null=True)),
                ('service_type', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_code', models.CharField(blank=True, max_length=100, null=True)),
                ('node', models.CharField(blank=True, max_length=100, null=True)),
                ('port_number', models.CharField(blank=True, max_length=50, null=True)),
                ('rdp_password', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('pb_id', models.CharField(blank=True, max_length=255, null=True)),
                ('pb_password', models.CharField(blank=True, max_length=255, null=True)),
                ('extension_number', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user_creation_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
