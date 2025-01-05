from django.urls import path
from custom.views import pages_profile_view,pages_invoice_view,pages_faq_view,pages_pricing_view,pages_maintenance_view,pages_starter_view,pages_preloader_view,pages_timeline_view,auth_login_view,auth_login2_view,auth_register_view,auth_register2_view,auth_logout_view,auth_logout2_view,auth_recoverpw_view,auth_recoverpw2_view,auth_lock_screen_view,auth_lock_screen2_view,auth_confirm_mail_view,auth_confirm_mail2_view,error_404_view,error_404_alt_view,error_500_view

urlpatterns = [

    # Pages
        path("profile", view=pages_profile_view, name="profile"),
        path("invoice", view=pages_invoice_view, name="invoice"),
        path("faq", view=pages_faq_view, name="faq"),
        path("pricing", view=pages_pricing_view, name="pricing"),
        path("maintenance", view=pages_maintenance_view, name="maintenance"),
        path("starter-page", view=pages_starter_view, name="starter"),
        path("preloader", view=pages_preloader_view, name="preloader"),
        path("timeline", view=pages_timeline_view, name="timeline"),
    
    # Auth Pages
        path("login", view=auth_login_view, name="login"),
        path("login-2", view=auth_login2_view, name="login-2"),
        path("register", view=auth_register_view, name="register"),
        path("register-2", view=auth_register2_view, name="register-2"),
        path("logout", view=auth_logout_view, name="logout"),
        path("logout-2", view=auth_logout2_view, name="logout-2"),
        path("recoverpw", view=auth_recoverpw_view, name="recoverpw"),
        path("recoverpw-2", view=auth_recoverpw2_view, name="recoverpw-2"),
        path("lock-screen", view=auth_lock_screen_view, name="lock-screen"),
        path("lock-screen-2", view=auth_lock_screen2_view, name="lock-screen-2"),
        path("confirm-mail", view=auth_confirm_mail_view, name="confirm-mail"),
        path("confirm-mail-2", view=auth_confirm_mail2_view, name="confirm-mail-2"),

    # Error Pages
        path("error-404", view=error_404_view, name="error-404"),
        path("error-404-alt", view=error_404_alt_view, name="error-404-alt"),
        path("error-500", view=error_500_view, name="error-500"),
]
