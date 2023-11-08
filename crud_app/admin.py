from django.contrib import admin
from .models import Task

# Register your models here.
#Model task showing in admin panel

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    
    
admin.site.register(Task, TaskAdmin)