from django.contrib import admin
from django.urls import path
from bradt import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.homepage.as_view(), name="homepage"),
    path("add-todo", core_views.add_todo, name="add_todo"),
    path("<int:id>/edit", core_views.edit.as_view(), name="edit"),
    path("delete/<int:id>", core_views.delete, name="delete"),
]
