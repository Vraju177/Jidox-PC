from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomView(LoginRequiredMixin,TemplateView):
    pass

#Pages
pages_profile_view = CustomView.as_view(template_name="custom/pages/pages-profile.html")
pages_invoice_view = CustomView.as_view(template_name="custom/pages/pages-invoice.html")
pages_faq_view = CustomView.as_view(template_name="custom/pages/pages-faq.html")
pages_pricing_view = CustomView.as_view(template_name="custom/pages/pages-pricing.html")
pages_maintenance_view = CustomView.as_view(template_name="custom/pages/pages-maintenance.html")
pages_starter_view = CustomView.as_view(template_name="custom/pages/pages-starter.html")
pages_preloader_view = CustomView.as_view(template_name="custom/pages/pages-preloader.html")
pages_timeline_view = CustomView.as_view(template_name="custom/pages/pages-timeline.html")

# Auth Pages
auth_login_view = CustomView.as_view(template_name="custom/auth-pages/auth-login.html")
auth_login2_view = CustomView.as_view(template_name="custom/auth-pages/auth-login-2.html")
auth_register_view = CustomView.as_view(template_name="custom/auth-pages/auth-register.html")
auth_register2_view = CustomView.as_view(template_name="custom/auth-pages/auth-register-2.html")
auth_logout_view = CustomView.as_view(template_name="custom/auth-pages/auth-logout.html")
auth_logout2_view = CustomView.as_view(template_name="custom/auth-pages/auth-logout-2.html")
auth_recoverpw_view = CustomView.as_view(template_name="custom/auth-pages/auth-recoverpw.html")
auth_recoverpw2_view = CustomView.as_view(template_name="custom/auth-pages/auth-recoverpw-2.html")
auth_lock_screen_view = CustomView.as_view(template_name="custom/auth-pages/auth-lock-screen.html")
auth_lock_screen2_view = CustomView.as_view(template_name="custom/auth-pages/auth-lock-screen-2.html")
auth_confirm_mail_view = CustomView.as_view(template_name="custom/auth-pages/auth-confirm-mail.html")
auth_confirm_mail2_view = CustomView.as_view(template_name="custom/auth-pages/auth-confirm-mail-2.html")

# Error Pages
error_404_view = CustomView.as_view(template_name="custom/error-pages/error-404.html")
error_404_alt_view = CustomView.as_view(template_name="custom/error-pages/error-404-alt.html")
error_500_view = CustomView.as_view(template_name="custom/error-pages/error-500.html")