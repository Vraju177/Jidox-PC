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

    full_name = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    user_creation_date = models.DateField(null=True, blank=True)  # Allow null or blank date
    status = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['full_name', 'node', 'service_type', 'user_creation_date', 'status']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
