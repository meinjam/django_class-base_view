from django.shortcuts import render, redirect
from .models import *
from django.views import View


class homepage(View):
    http_method_names = ["get", "post", "put", "delete"]

    def get(self, request):
        todos = Todos.objects.order_by("-id")
        print(todos)
        return render(request, "todos/index.html", context={"todos": todos})

    def post(self, request):
        table = Todos()
        table.todo = request.POST.get("todo")
        table.save()
        return redirect("homepage")


def add_todo(request):
    return render(request, "todos/create.html")


class edit(View):
    http_method_names = ["get", "post", "put", "delete"]

    def get(self, request, id):
        todo = Todos.objects.get(pk=id)
        print("todo")
        return render(request, "todos/edit.html", context={"todo": todo})

    def post(self, request, id):
        todo = Todos.objects.filter(pk=id).first()
        todo.todo = request.POST.get("todo")
        todo.save()
        return redirect("homepage")


def delete(request, id):
    todo = Todos.objects.get(pk=id)
    todo.delete()
    return redirect("homepage")
