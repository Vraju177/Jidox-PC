from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User model."""
    
    # First and last name are replaced by a custom name field
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    # User fields
    username = models.CharField(max_length=150, unique=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=100)  # Required
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    alternate_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email_password = models.CharField(max_length=255, null=True, blank=True)
    service_type = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    branch_code = models.CharField(max_length=100, null=True, blank=True)
    node = models.CharField(max_length=100, null=True, blank=True)
    port_number = models.CharField(max_length=50, null=True, blank=True)
    rdp_password = models.CharField(max_length=255, null=True, blank=True)
    internal_ip = models.GenericIPAddressField(null=True, blank=True)
    pb_id = models.CharField(max_length=255, null=True, blank=True)
    pb_password = models.CharField(max_length=255, null=True, blank=True)
    extension_number = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    user_creation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    # Fields required during user creation
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


# Model for billing tables-

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class BillingModel(models.Model):
    """Model to store billing-related information."""

    client_name = models.CharField(_("Client Name"), max_length=255)
    client_address = models.TextField(_("Client Address"), blank=True, null=True)
    billing_to = models.CharField(_("Billing To"), max_length=255, blank=True, null=True)
    service_type = models.CharField(_("Service Type"), max_length=100, blank=True, null=True)
    bill_description = models.TextField(_("Bill Description"), blank=True, null=True)
    ticket_id = models.CharField(_("Ticket ID"), max_length=50, blank=True, null=True)
    emailed = models.BooleanField(_("Emailed"), default=False)
    comments = models.TextField(_("Comments"), blank=True, null=True)
    billing_date = models.DateField(_("Created Date"), auto_now_add=True)
    invoice_no = models.CharField(_("Invoice Number"), max_length=250, blank=True, null=True)
    #invoice_date = models.CharField(_("Invoice Date"), max_length=50, blank=True, null=True)
    invoice_date = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name = _("Billing Model")
        verbose_name_plural = _("Billing Models")





from django.utils.translation import gettext_lazy as _

class InventoryModel(models.Model):
    """Model to store inventory-related information."""
    
    manufacturer = models.CharField(_("Manufacturer"), max_length=255)
    product_item = models.CharField(_("Product Item"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    total_ins = models.PositiveIntegerField(_("Total In Stock"), default=0)
    total_outs = models.PositiveIntegerField(_("Total Out Stock"), default=0)
    date_out = models.DateField(_("Date Out"), blank=True, null=True)
    stock_inhand = models.PositiveIntegerField(_("Stock In Hand"), default=0)
    sr_no = models.CharField(_("Serial Number"), max_length=255)
    mac_product_no = models.CharField(_("MAC Product No"), max_length=100, blank=True, null=True)
    to_user = models.CharField(_("To User"), max_length=255, blank=True, null=True)
    to_client = models.CharField(_("To Client"), max_length=255, blank=True, null=True)
    ticket_id = models.CharField(_("Ticket ID"), max_length=50, blank=True, null=True)
    inventory_comments = models.TextField(_("Inventory Comments"), blank=True, null=True)
    created_date = models.DateField(_("Created Date"), auto_now_add=True)
    
    def __str__(self):
        return f"{self.product_item} - {self.manufacturer}"
    
    class Meta:
        verbose_name = _("Inventory Model")
        verbose_name_plural = _("Inventory Models")
        ordering = ["-created_date"]


#=================== NEW Stock Inventory Pages Model with SIGNALS-----------------------------------
from django.db import models

# StockInModel: Recording Incoming Stock
class StockInModel(models.Model):
    manufacturer = models.CharField(max_length=255)
    product_item = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    total_stock_received = models.PositiveIntegerField(default=0)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    mac_product_no = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    stock_in_date = models.DateField(auto_now_add=True)  # Auto-filled with the current date

    def __str__(self):
        return f"{self.product_item} - Received: {self.total_stock_received}"

# StockOutModel: Recording Outgoing Stock
class StockOutModel(models.Model):
    manufacturer = models.CharField(max_length=255)
    product_item = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    total_stock_sent = models.PositiveIntegerField()
    stock_out_date = models.DateField(auto_now_add=True)  # Auto-filled with the current date
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    mac_product_no = models.CharField(max_length=255, blank=True, null=True)
    to_user = models.CharField(max_length=255, blank=True, null=True)
    to_client = models.CharField(max_length=255, blank=True, null=True)
    ticket_id = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    stock_in_date = models.DateField()  # Extracted from StockInModel

    def __str__(self):
        return f"{self.product_item} - Sent: {self.total_stock_sent}"


# StockInHand: Tracks Available Stock
class StockInHand(models.Model):
    product_item = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    total_stock_received = models.PositiveIntegerField(default=0)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    mac_product_no = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    received_from = models.CharField(max_length=255, blank=True, null=True)
    stock_in_date = models.DateField()
    stock_in_hand = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product_item} - Stock: {self.stock_in_hand}"

    def update_stock(self, quantity):
        """Method to update the stock level in hand."""
        self.stock_in_hand += quantity
        self.save()


class InventoryHistory(models.Model):
    TRANSACTION_CHOICES = [
        ('Stock In', 'Stock In'),
        ('Stock Out', 'Stock Out'),
    ]
    
    product_item = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    quantity = models.IntegerField()
    serial_no = models.CharField(max_length=255, null=True, blank=True)  # New field for serial number
    mac_product_no = models.CharField(max_length=255, null=True, blank=True)
    received_from = models.CharField(max_length=255, null=True, blank=True)  # e.g., supplier, warehouse
    delivered_to = models.CharField(max_length=255, null=True, blank=True)  # e.g., client, department
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    ticket_id = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_item} - {self.transaction_type} ({self.transaction_date})"
