from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'full_description', 'status', 'execution_date']
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['description', 'full_description']
    fields = ['description', 'full_description', 'status', 'execution_date']


admin.site.register(Task, TaskAdmin)
