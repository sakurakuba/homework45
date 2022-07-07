from django.contrib import admin

# Register your models here.
from todo.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'deadline']
    list_display_links = ['description']
    list_filter = ['deadline']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'deadline', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
