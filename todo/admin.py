from django.contrib import admin
from .models import Task, Photo

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'priority', 'complete', 'created_at', 'updated_at', 'user')
    list_filter = ('priority', 'complete', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'description', 'due_date', 'priority', 'complete', 'created_at', 'updated_at', 'user')
    readonly_fields = ('created_at', 'updated_at')
    # set the default ordering higher to lower
    ordering = ('priority',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Photo)
