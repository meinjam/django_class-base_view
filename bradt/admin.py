from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    search_fields = ("todo",)
    list_display = ("todo", "created_at", "id")


admin.site.register(Todos, TodosAdmin)
