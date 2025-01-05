from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Choices for the 'emailed' field in Billing
EMAILED_CHOICES = [
    ('YES', 'Yes'),
    ('NO', 'No'),
]


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


# Model for tables-
class BillingModel(models.Model):
    """Model for Billing records."""

    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    billing_to = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    bill_description = models.CharField(max_length=255)
    ticket_id = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    emailed = models.CharField(
        max_length=3,
        choices=EMAILED_CHOICES,
        default='NO',
    )
    comments = models.CharField(max_length=255, default='No Comments')
    invoice_no = models.IntegerField(null=True, blank=True, default=None)
    invoice_date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.client_name} - {self.service_type}'