from django.urls import path
from apps.views import apps_calendar_view, apps_chat_view, apps_email_inbox_view,apps_email_read,apps_tasks,apps_tasks_details,apps_kanban_board,apps_file_manager

urlpatterns = [
    # Calaendar
    path("calendar", view=apps_calendar_view, name="calendar"),
    # Chat
    path("chat", view=apps_chat_view, name="chat"),
    # Email
    path("email-inbox", view=apps_email_inbox_view, name="email-inbox"),
    path("email-read", view=apps_email_read, name="email-read"),
    # Tasks
    path("tasks", view=apps_tasks, name="tasks"),
    path("tasks-details", view=apps_tasks_details, name="tasks-details"),
    # Kanban
    path("kanban-board", view=apps_kanban_board, name="kanban"),
    # File Manager
    path("file-manager", view=apps_file_manager, name="file-manager"),

]
