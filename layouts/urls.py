from django.urls import path
from layouts.views import horizontal_view,detached_view,full_view,fullscreen_view,hover_view,compact_view,icon_view

urlpatterns = [

    # Layouts
        path("horizontal", view=horizontal_view, name="horizontal"),
        path("detached", view=detached_view, name="detached"),
        path("full", view=full_view, name="full"),
        path("fullscreen", view=fullscreen_view, name="fullscreen"),
        path("hover", view=hover_view, name="hover"),
        path("compact", view=compact_view, name="compact"),
        path("icon-view", view=icon_view, name="icon-view"),
]
