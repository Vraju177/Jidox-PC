from django.urls import path
from . import views

app_name = "users"  # Ensure app namespace is set for reverse URL lookup

urlpatterns = [
    # URL for table view (with trailing slash)
    path('tables/billing/', views.billing_table_view, name='billing_table'),
    path('components/tables-datatable/', views.user_table_view, name='components_table_datatable_with_slash'),  

    path('inventory/stock-in/', views.stock_in_view, name='stock_in_view'),
    path('inventory/stock-out/', views.stock_out_view, name='stock_out_view'),
    #path('inventory/', views.inventory_view, name='inventory'),
    path('inventory/', views.inventory_dashboard, name='inventory_dashboard'),  # Inventory Dashboard view with both Stock In and Stock Out forms

     # New URL for form-billing.html
    path('forms/billing/create/', views.create_billing, name='create_billing'),
    # URL for user details (can be used for AJAX request to fetch full user details)
    path('user/<int:user_id>/details/', views.user_details_view, name='user_details'),  

    # Dashboard Stats Displays
    path('get_stats/', views.get_stats, name='get_stats'),
    path('get_all_clients_stats/', views.get_all_clients_stats, name='get_all_clients_stats'),

    # Inventorymodel
    path('inventory/create/', views.create_inventory, name='create_inventory'),
    path('inventory/table', views.inventory_table_view, name='inventory_table'),


    path('<str:username>/', views.user_detail_view, name='detail'),
    path("~redirect/", view=views.user_redirect_view, name="redirect"),
    path("~update/", view=views.user_update_view, name="update"),
    path("create_user/", views.create_user, name="create_user"),
    
]
