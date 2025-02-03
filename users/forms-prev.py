from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as admin_forms
from django.utils.translation import gettext_lazy as _
from .models import User
from django.core.exceptions import ValidationError
from datetime import datetime


User = get_user_model()


# Custom User Change Form for admin
class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


# Custom User Creation Form for admin
class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


# UserForm for creating and updating users outside of the admin
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'node', 'service_type', 'user_creation_date', 'status']

    def clean_user_creation_date(self):
        date_str = self.cleaned_data.get('user_creation_date')
        if date_str:
            try:
                # Check if the date format is correct
                user_creation_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")
            return user_creation_date
        return None  # If no date is provided, return None (optional handling)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('This username is already taken.'))
        return username


# For BillingModel
from django import forms
from .models import BillingModel
from django.core.exceptions import ValidationError
from datetime import datetime

class BillingModelForm(forms.ModelForm):
    class Meta:
        model = BillingModel
        fields = [
            'client_name',
            'client_address',
            'billing_to',
            'service_type',
            'bill_description',
            'ticket_id',
            'emailed',
            'comments',
            'invoice_no',
            'invoice_date',
        ]

    def clean_invoice_date(self):
        invoice_date = self.cleaned_data.get('invoice_date')
        if invoice_date and invoice_date > datetime.now().date():
            raise ValidationError("Invoice date cannot be in the future.")
        return invoice_date

    def clean_ticket_id(self):
        ticket_id = self.cleaned_data.get('ticket_id')
        if ticket_id and ticket_id < 0:
            raise ValidationError("Ticket ID must be a positive integer.")
        return ticket_id



