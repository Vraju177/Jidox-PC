# jidox/urls.py

from django.contrib import admin
from django.urls import path, include
from jidox.view import index_view  # Import the index view
from users.views import user_table_view  # (Optional) Import only if explicitly required here

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),

    # Dashboard (homepage)
    path("", view=index_view, name="index"),

    # Users app URLs (ensuring there is only one mapping)
    #path("users/", include("users.urls", namespace="users")),  
    path('users/', include('users.urls')),

    # Apps URLs
    path("apps/", include("apps.urls")),

    # Custom URLs
    path("custom/", include("custom.urls")),

    # Layouts URLs
    path("layouts/", include("layouts.urls")),

    # Components URLs
    path("components/", include("components.urls")),

    # Django Allauth (for authentication)
    path("accounts/", include("allauth.urls")),
]
