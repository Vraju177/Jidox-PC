from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .forms import UserForm
from .models import BillingModel
from .forms import BillingModelForm
from django.contrib import messages
from django.db.models import Q
import logging

User = get_user_model()


# User Detail View (already implemented correctly)
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


# User Update View (updates the logged-in user's information)
class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


# User Redirect View (for redirection)
class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


# Handle creating a user from a form using AJAX
# users/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import User  # Assuming you have a User model

def create_user(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        node = request.POST.get('node')
        service_type = request.POST.get('service_type')
        user_creation_date = request.POST.get('user_creation_date')
        status = request.POST.get('status')

        if not (full_name and username and node and service_type and user_creation_date and status):
            return JsonResponse({'message': 'All fields are required!'}, status=400)

        user = User.objects.create(
            full_name=full_name,
            username=username,
            node=node,
            service_type=service_type,
            user_creation_date=user_creation_date,
            status=status
        )

        return JsonResponse({'message': 'User created successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=400)




from django.http import JsonResponse
from django.views import View
from .models import User
import datetime

class UserDataTableView(View):
    def get(self, request):
        users = User.objects.all().values('full_name', 'username', 'node', 'service_type', 'user_creation_date', 'status')

        data = []
        for user in users:
            data.append({
                'full_name': user['full_name'],
                'username': user['username'],
                'node': user['node'],
                'service_type': user['service_type'],
                'user_creation_date': user['user_creation_date'].strftime('%Y-%m-%d') if user['user_creation_date'] else '',  # Handle nulls correctly
                'status': user['status']
            })

        return JsonResponse({'data': data})

from django.shortcuts import render
from .models import User

def user_table_view(request):
    # Fetch selected fields for table view
    users = User.objects.all().values(
        'id', 'username', 'full_name', 'company', 'service_type', 'phone_number', 'email', 'node', 'port_number', 'extension_number', 'status'
    )
    
    # Render the page with the fetched data
    return render(request, 'components/tables/tables-datatable.html', {'users': users})

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User  # Replace with your custom user model if it's not the default

def user_details_view(request, user_id):
    # Get the user object or return a 404 error if not found
    user = get_object_or_404(User, id=user_id)
    
    # Return the user details in JSON format
    data = {
        'username': user.username,
        'full_name': user.full_name,
        'company': user.company,
        'service_type': user.service_type,
        'phone_number': user.phone_number,
        'alternate_number': user. alternate_number,
        'location': user.location,
        'branch_code': user.branch_code,
        'email': user.email,
        'email_password': user.email_password,
        'node': user.node,
        'port_number': user.port_number,
        'rdp_password': user.rdp_password,
        'internal_ip': user.internal_ip,
        'pb_id': user.pb_id,
        'pb_password': user.pb_password,
        'extension_number': user.extension_number,
        'status': user.status,
        'notes': user.notes,
        'user_creation_date': user.user_creation_date.strftime('%d-%m-%Y'),  # Format the date if necessary
    }
    
    return JsonResponse(data)



from django.http import JsonResponse
from django.shortcuts import render
from .models import User

def get_stats(request):
    client_name = request.GET.get('client_name')
    print("Client_name:", client_name)

    # Case when 'client_name' is provided or 'Total' is selected
    if client_name:
        client_name = client_name.strip()

        if client_name == "All Clients":
            # Calculate totals for all clients
            stats = {
                'active_users': User.objects.exclude(full_name__isnull=True).exclude(full_name='').count(),
                'active_rdp': User.objects.exclude(node__isnull=True).exclude(node='').count(),
                'active_emails': User.objects.exclude(email__isnull=True).exclude(email='').count(),
                'active_voip': User.objects.exclude(extension_number__isnull=True).exclude(extension_number='').count(),
            }
        else:
            # Filter by client name if specific client is selected
            stats = {
                'active_users': User.objects.filter(company__iexact=client_name)
                    .exclude(full_name__isnull=True).exclude(full_name='').count(),
                'active_rdp': User.objects.filter(company__iexact=client_name)
                    .exclude(node__isnull=True).exclude(node='').count(),
                'active_emails': User.objects.filter(company__iexact=client_name)
                    .exclude(email__isnull=True).exclude(email='').count(),
                'active_voip': User.objects.filter(company__iexact=client_name)
                    .exclude(extension_number__isnull=True).exclude(extension_number='').count(),
            }

        # Fetch the first service_type if available for the selected client
        first_service_type = User.objects.filter(company__iexact=client_name).values('service_type').first()
        service_type = first_service_type['service_type'] if first_service_type else None

        # Return the response with stats and service_type
        return JsonResponse({
            'stats': stats,         # Stats dictionary (active_users, active_rdp, etc.)
            'service_type': service_type  # The extracted service_type
        })
    else:
        # If no 'client_name' is provided in the request, return an error
        return JsonResponse({'error': 'Invalid client name'}, status=400)


def get_all_clients_stats(request):
    # Get all unique client names
    client_names = User.objects.values_list('company', flat=True).distinct()

    # Initialize dictionary for aggregate stats
    total_stats = {
        'active_users': 0,
        'active_rdp': 0,
        'active_emails': 0,
        'active_voip': 0,
    }

    client_stats = []

    for client_name in client_names:
        stats = {
            'client_name': client_name,
            'active_users': User.objects.filter(company__iexact=client_name)
                .exclude(full_name__isnull=True).exclude(full_name='').count(),
            'active_rdp': User.objects.filter(company__iexact=client_name)
                .exclude(node__isnull=True).exclude(node='').count(),
            'active_emails': User.objects.filter(company__iexact=client_name)
                .exclude(email__isnull=True).exclude(email='').count(),
            'active_voip': User.objects.filter(company__iexact=client_name)
                .exclude(extension_number__isnull=True).exclude(extension_number='').count(),
        }
        
        # Aggregate stats
        total_stats['active_users'] += stats['active_users']
        total_stats['active_rdp'] += stats['active_rdp']
        total_stats['active_emails'] += stats['active_emails']
        total_stats['active_voip'] += stats['active_voip']

        client_stats.append(stats)

    return JsonResponse({
        'clients': client_stats,  # Stats per client
        'totalStats': total_stats  # Total aggregated stats
    })


#================================================================================
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from .models import BillingModel

@require_http_methods(["GET", "POST"])
@csrf_exempt
def create_billing(request):
    if request.method == 'GET':
        return render(request, 'components/forms/form-billing.html')

    if request.method == 'POST':
        try:
            # Handle both JSON and form data submissions
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            # Extract billing data
            client_name = data.get('client_name')
            client_address = data.get('client_address')
            billing_to = data.get('billing_to')
            service_type = data.get('service_type') or ''  # Optional
            bill_description = data.get('bill_description')
            ticket_id = data.get('ticket_id')
            emailed = data.get('emailed', '0')  # Default if not provided
            comments = data.get('comments') or ''  # Optional
            invoice_no = data.get('invoice_no') or ''  # Optional
            invoice_date = data.get('invoice_date') or None  # Optional

            # Handle the emailed checkbox
            emailed = '1' if emailed == 'on' else '2'

            # ✅ Validate only the mandatory fields
            if not client_name or not client_address or not billing_to or not bill_description or not ticket_id:
                return JsonResponse({'error': 'Missing required fields.'}, status=400)

            # Convert invoice_date to a datetime object, if provided
            if invoice_date:
                invoice_date = datetime.strptime(invoice_date, '%Y-%m-%d').date()

            # Save the billing record
            billing_record = BillingModel(
                client_name=client_name,
                client_address=client_address,
                billing_to=billing_to,
                service_type=service_type,
                bill_description=bill_description,
                ticket_id=ticket_id,
                emailed=emailed,
                comments=comments,
                invoice_no=invoice_no,
                invoice_date=invoice_date
            )

            billing_record.save()
            print(f"Billing record saved: {billing_record}")

            return JsonResponse({
                'message': 'Billing record created successfully!',
                'data': model_to_dict(billing_record)
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': f'Error processing request: {str(e)}'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)




def billing_table_view(request):
    billings = BillingModel.objects.all()  # Get all records
    billing_data = [
        {
            'client_name': billing.client_name,
            'client_address': billing.client_address,
            'billing_to': billing.billing_to,
            'service_type': billing.service_type,
            'bill_description': billing.bill_description,
            'ticket_id': billing.ticket_id,
            'comments': billing.comments,
            'emailed': billing.emailed,
            'invoice_no': billing.invoice_no,
            'billing_date': billing.billing_date,
            'invoice_date': billing.invoice_date,
        }
        for billing in billings
    ]
    return render(request, "components/tables/tables-billing.html", {"billing_data": billing_data})



# =========================================================================

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import InventoryModel  # Assuming your Inventory model is named InventoryModel
from django.forms.models import model_to_dict

@require_http_methods(["GET", "POST"])
@csrf_exempt  # Use only if CSRF issues arise during testing (not recommended for production)
def create_inventory(request):
    """
    Handle GET and POST requests for creating an inventory record.
    """
    if request.method == 'GET':
        # Render the inventory form (HTML page)
        return render(request, 'components/forms/form-inventory.html')

    if request.method == 'POST':
        try:
            # Handle both JSON and form data submissions
            if request.content_type == 'application/json':
                # Parse JSON data
                data = json.loads(request.body)
            else:
                # Use `request.POST` for form-encoded data
                data = request.POST

            # Extract inventory data
            manufacturer = data.get('manufacturer')
            product_item = data.get('product_item')
            description = data.get('description')
            total_ins = data.get('total_ins')
            total_outs = data.get('total_outs')
            stock_inhand = data.get('stock_inhand')
            sr_no = data.get('sr_no')
            mac_product_no = data.get('mac_product_no')
            ticket_id = data.get('ticket_id')
            inventory_comments = data.get('inventory_comments')

            # Validate the required fields
            if not manufacturer or not product_item or not description or not total_ins or not total_outs or not sr_no or not ticket_id:
                return JsonResponse({'error': 'Missing required fields.'}, status=400)

            # Simulate saving the data to the database (replace with actual DB operations)
            inventory_data = {
                'manufacturer': manufacturer,
                'product_item': product_item,
                'description': description,
                'total_ins': total_ins,
                'total_outs': total_outs,
                'stock_inhand': stock_inhand,
                'sr_no': sr_no,
                'mac_product_no': mac_product_no,
                'ticket_id': ticket_id,
                'inventory_comments': inventory_comments,
            }

            inventory_record = InventoryModel(**inventory_data)

            # Debug message for development
            print(f"Inventory record created: {inventory_record}")
         
            # Save the inventory record to the database
            try:
                inventory_record.save()
                print(f"Inventory record saved: {inventory_record}")
            except Exception as e:
                import traceback
                print(f"Error saving inventory record: {e}")
                traceback.print_exc()  # Prints full error stack trace
            
            # Return success response
            return JsonResponse({
                'message': 'Inventory record created successfully!',
                'data': model_to_dict(inventory_record)
            }, status=200)

        except Exception as e:
            # Handle errors gracefully
            return JsonResponse({'error': f'Error processing request: {str(e)}'}, status=400)

    # Return 405 if the method is not allowed (optional, as require_http_methods ensures this)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)



from django.shortcuts import render
from .models import InventoryModel

def inventory_table_view(request):
    inventory_list = InventoryModel.objects.all()  # Get all inventory records
    inventory_list = [
        {
            'manufacturer': inventory.manufacturer,
            'product_item': inventory.product_item,
            'description': inventory.description,
            'total_ins': inventory.total_ins,
            'total_outs': inventory.total_outs,
            'stock_inhand': inventory.stock_inhand,
            'sr_no': inventory.sr_no,
            'mac_product_no': inventory.mac_product_no,
            'ticket_id': inventory.ticket_id,
            'inventory_comments': inventory.inventory_comments,
            'created_date': inventory.created_date,
        }
        for inventory in inventory_list
    ]
    return render(request, "components/tables/table-inventory.html", {"inventory_list": inventory_list})



# ------------------- NEW Stock inventory Pages-------------------
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import StockInForm, StockOutForm
from .models import StockInModel, StockOutModel, StockInHand, InventoryHistory
from django.db import transaction

# View to handle Stock In
def stock_in_view(request):
    if request.method == 'POST':
        form = StockInForm(request.POST)
        if form.is_valid():
            product_item = form.cleaned_data['product_item']
            manufacturer = form.cleaned_data['manufacturer']
            total_stock_received = form.cleaned_data['total_stock_received']
            serial_no = form.cleaned_data.get('serial_no')
            mac_product_no = form.cleaned_data.get('mac_product_no')
            description = form.cleaned_data.get('description')
            comments = form.cleaned_data.get('comments')

            # Use atomic transaction to ensure both models are updated
            with transaction.atomic():
                # Save to StockInModel
                stock_in = form.save()

                # Update or create entry in StockInHand
                stock_in_hand, created = StockInHand.objects.get_or_create(
                    product_item=product_item,
                    manufacturer=manufacturer,
                    stock_in_date=stock_in.stock_in_date
                )
                stock_in_hand.total_stock_received += total_stock_received
                stock_in_hand.stock_in_hand += total_stock_received
                stock_in_hand.save()

                # Record the transaction in InventoryHistory
                InventoryHistory.objects.create(
                    product_item=product_item,
                    manufacturer=manufacturer,
                    transaction_type='Stock In',
                    quantity=total_stock_received,
                    serial_no=serial_no,
                    mac_product_no=mac_product_no,
                    received_from='Supplier',  # You can modify this based on your requirements
                    transaction_date=stock_in.stock_in_date,
                    description=description,
                    ticket_id=None,  # You can add this logic based on your requirements
                    comments=comments
                )

            messages.success(request, 'Stock In successful!')
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Error with the form data.')
            return JsonResponse({'success': False})

    else:
        form = StockInForm()
    return render(request, 'components/tables/inventory.html', {'form': form})

# View to handle Stock Out
def stock_out_view(request):
    if request.method == 'POST':
        form = StockOutForm(request.POST)
        if form.is_valid():
            product_item = form.cleaned_data['product_item']
            manufacturer = form.cleaned_data['manufacturer']
            total_stock_sent = form.cleaned_data['total_stock_sent']
            serial_no = form.cleaned_data.get('serial_no')
            mac_product_no = form.cleaned_data.get('mac_product_no')
            to_user = form.cleaned_data.get('to_user')
            to_client = form.cleaned_data.get('to_client')
            ticket_id = form.cleaned_data.get('ticket_id')
            comments = form.cleaned_data.get('comments')

            # Use atomic transaction to ensure both models are updated
            with transaction.atomic():
                # Save to StockOutModel
                stock_out = form.save()

                # Update StockInHand table (reduce stock)
                stock_in_hand = StockInHand.objects.get(product_item=product_item, manufacturer=manufacturer)
                stock_in_hand.stock_in_hand -= total_stock_sent
                stock_in_hand.save()

                # Record the transaction in InventoryHistory
                InventoryHistory.objects.create(
                    product_item=product_item,
                    manufacturer=manufacturer,
                    transaction_type='Stock Out',
                    quantity=total_stock_sent,
                    serial_no=serial_no,
                    mac_product_no=mac_product_no,
                    delivered_to=to_user or to_client,  # You can modify this based on your requirements
                    transaction_date=stock_out.stock_out_date,
                    description=None,  # You can modify this based on your requirements
                    ticket_id=ticket_id,
                    comments=comments
                )

            messages.success(request, 'Stock Out successful!')
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Error with the form data.')
            return JsonResponse({'success': False})

    else:
        form = StockOutForm()
    return render(request, 'components/tables/inventory.html', {'form': form})

def inventory_view(request):
    stock_in_hand_data = StockInHand.objects.all()
    inventoryhistory_data = InventoryHistory.objects.all().order_by('-transaction_date')
    return render(request, 'components/tables/inventory.html', {
        'stock_in_hand_data': stock_in_hand_data,
        'inventoryhistory_data': inventoryhistory_data,
    })
