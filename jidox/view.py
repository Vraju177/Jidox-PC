from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin,TemplateView):
     pass

index_view = DashboardView.as_view(template_name="index.html")
