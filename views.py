from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo.forms import ToDoForm
from todo.models import ToDo


def index(request):
    todo = ToDo.objects.all()
    form = ToDoForm()

    context = {
        'todos': todo,
        'form': form
    }
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    def form_valid(self):
        form = ToDo
        form.instance.author = request.user
        return super().form_valid(form)

    return render(request, 'todo/index.html', context)


def update(request, pk):
    form = ToDo.objects.get(id=pk)

    todo_form = ToDoForm(instance=form)

    context = {
        'form': todo_form
    }
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'todo/update.html', context)


def delete(request, pk):
    item = ToDo.objects.get(id=pk)

    context = {
        'item': item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request, 'todo/delete.html', context)
