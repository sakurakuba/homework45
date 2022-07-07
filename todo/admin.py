from django.contrib import admin

# Register your models here.
from todo.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'deadline']
    list_display_links = ['title']
    list_filter = ['deadline']
    search_fields = ['description', 'status']
    fields = ['title', 'description', 'status', 'deadline', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
