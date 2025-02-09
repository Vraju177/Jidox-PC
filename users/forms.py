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
        if ticket_id:
            try:
                ticket_id_int = int(ticket_id)
                if ticket_id_int < 0:
                    raise ValidationError("Ticket ID must be a positive integer.")
            except ValueError:
                raise ValidationError("Ticket ID must be a valid number.")
        return ticket_id



#------------------ For NEW Stock Inventory Pages--------------------
from django import forms
from .models import StockInModel, StockOutModel

PRODUCT_CHOICES = [
    ("Laptop - Non-touch", "Laptop - Non-touch"),
    ("Laptop - Touch", "Laptop - Touch"),
    ("Laptop - Adaptors", "Laptop - Adaptors"),
    ("LCD Monitor", "LCD Monitor"),
    ("CPU", "CPU"),
    ("Switches", "Switches"),
    ("Keyboard", "Keyboard"),
    ("Mouse", "Mouse"),
    ("Voip Phone", "Voip Phone"),
    ("Voip - Adaptors", "Voip - Adaptors"),
    ("Others", "Others"),
]

# Form for Stock In
class StockInForm(forms.ModelForm):
    product_item = forms.ChoiceField(choices=PRODUCT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  
    total_stock_received = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    serial_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mac_product_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    received_from = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = StockInModel
        fields = [  # Do not include stock_in_date here
            'product_item', 'manufacturer', 'total_stock_received',
            'serial_no', 'mac_product_no', 'description', 'received_from'
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        # No need to manually set stock_in_date, as it will be set automatically
        if commit:
            instance.save()
        return instance


# Form for Stock Out
class StockOutForm(forms.ModelForm):
    product_item = forms.ChoiceField(choices=PRODUCT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  
    total_stock_sent = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    serial_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mac_product_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    to_user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    to_client = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ticket_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)

    class Meta:
        model = StockOutModel
        fields = [  # Exclude stock_out_date as it's auto-generated
            'product_item', 'manufacturer', 'total_stock_sent',
            'serial_no', 'mac_product_no', 'description',
            'to_user', 'to_client', 'ticket_id', 'comments'
        ]

    def __init__(self, *args, **kwargs):
        super(StockOutForm, self).__init__(*args, **kwargs)
        self.fields['product_item'].required = True
        self.fields['manufacturer'].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        # No need to manually set stock_out_date, it will be set automatically in the model
        if commit:
            instance.save()
        return instance