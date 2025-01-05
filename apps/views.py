from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AppsView(LoginRequiredMixin,TemplateView):
    pass


# Calendar
apps_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# Chat
apps_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")
# Mail Box
apps_email_inbox_view = AppsView.as_view(template_name="apps/apps-email-inbox.html")
apps_email_read = AppsView.as_view(template_name="apps/apps-email-read.html")
# Tasks
apps_tasks = AppsView.as_view(template_name="apps/apps-tasks.html")
apps_tasks_details = AppsView.as_view(template_name="apps/apps-tasks-details.html")
# Kanban
apps_kanban_board = AppsView.as_view(template_name="apps/apps-kanban.html")
# File Manager
apps_file_manager = AppsView.as_view(template_name="apps/apps-file-manager.html")