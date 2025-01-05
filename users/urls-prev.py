from django.urls import path, include
from . import views
from .views import get_stats


from .views import (
    user_redirect_view,
    user_update_view,
    user_details_view,  # Import the new view
)

app_name = "users"  # Ensure app namespace is set for reverse URL lookup

urlpatterns = [
    # URL for table view (with trailing slash)
    path('components/tables-datatable/', views.user_table_view, name='components_table_datatable_with_slash'),  
    
    # URL for user details (can be used for AJAX request to fetch full user details)
    path('user/<int:user_id>/details/', views.user_details_view, name='user_details'),  # Updated to pass user ID. This URL is for AJAX call

    # Existing URLs
    path('<str:username>/', views.user_detail_view, name='detail'),
    path("~redirect/", view=views.user_redirect_view, name="redirect"),
    path("~update/", view=views.user_update_view, name="update"),
    path("/create_user/", views.create_user, name="create_user"),

    # Stats URL (the one used by AJAX)
    path('get_stats/', get_stats, name='get_stats'),
]
