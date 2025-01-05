from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LayoutView(LoginRequiredMixin,TemplateView):
    pass

# Layouts
horizontal_view = LayoutView.as_view(template_name="custom/layouts/horizontal.html")
detached_view = LayoutView.as_view(template_name="custom/layouts/detached.html")
full_view = LayoutView.as_view(template_name="custom/layouts/full.html")
fullscreen_view = LayoutView.as_view(template_name="custom/layouts/fullscreen.html")
hover_view = LayoutView.as_view(template_name="custom/layouts/hover.html")
compact_view = LayoutView.as_view(template_name="custom/layouts/compact.html")
icon_view = LayoutView.as_view(template_name="custom/layouts/icon-view.html")
