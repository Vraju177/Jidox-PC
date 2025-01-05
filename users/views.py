from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .forms import UserForm


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
        'email': user.email,
        'node': user.node,
        'port_number': user.port_number,
        'extension_number': user.extension_number,
        'status': user.status,
        'notes': user.notes,
        'user_creation_date': user.user_creation_date.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date if necessary
    }
    
    return JsonResponse(data)





from django.http import JsonResponse
from django.shortcuts import render
from .models import User

def get_stats(request):
    #print("Client_name1",client_name)

    client_name = request.GET.get('client_name')
    print("Client_name2",client_name)
  
    if client_name:
        # Remove any leading/trailing spaces and handle case-insensitive matching
        client_name = client_name.strip()
        print("Client_name",client_name)

        stats = {
            'active_users': User.objects.filter(company__iexact=client_name)  # Case-insensitive match for company
                .exclude(full_name__isnull=True)
                .exclude(full_name='')
                #.print(f"Active users count for '{client_name}': {active_users.count()}"),
                .count(),
            'active_rdp': User.objects.filter(company__iexact=client_name)  # Case-insensitive match for company
                .exclude(node__isnull=True)
                .exclude(node='')
                .count(),
            'active_emails': User.objects.filter(company__iexact=client_name)  # Case-insensitive match for company
                .exclude(email__isnull=True)
                .exclude(email='')
                .count(),
            'active_voip': User.objects.filter(company__iexact=client_name)  # Case-insensitive match for company
                .exclude(extension_number__isnull=True)
                .exclude(extension_number='')
                .count(),
            }
        #print(f"Active users count: {active_users}")  
        return JsonResponse({'stats': stats})
    else:
        return JsonResponse({'error': 'Client name not provided or invalid'}, status=400)



