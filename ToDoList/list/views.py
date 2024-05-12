from django.shortcuts import render, redirect
from .models import TasksModel
from .forms import TasksForm

def index(request):
    object_list = TasksModel.objects.all()
    form = TasksForm()
    print(object_list.first().status)
    return render(request, "index.html", {"list": object_list, 'form': form})

def delete_view(request, id):
    task = TasksModel.objects.get(id=id)
    task.delete()
    return redirect('/')

def change_view(request, id):
    task = TasksModel.objects.get(id=id)
    task.status = request.GET.get('status')
    task.save()
    # form = TasksForm(request.GET)
    # if form.is_valid():
    #     form.save()
    return redirect('/')