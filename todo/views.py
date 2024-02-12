from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import TaskForm,LoginForm,PhotoForm,UsercreateForm
from django.shortcuts import redirect
from django.contrib.auth.models import auth

from .models import Task,Photo



def register(request):
    form = UsercreateForm
    if request.method == "POST":
        form = UsercreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "register.html", {"form": form})


def login(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print("User found")
                auth.login(request, user)
                print("User logged in")
                tasks = Task.objects.filter(user=request.user)
                return render(request, "dashboard.html", {"tasks": tasks})
        
            else:
                print("Invalid credentials")
    return render(request, "index.html", {"form": form})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if form.is_valid() and photo_form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
            photo = photo_form.save(commit=False)
            photo.task = task
            photo.save()
            return redirect("dashboard")
    else:
        form = TaskForm()
        photo_form = PhotoForm()
        
    return render(request, "create_task.html", {"form": form, "photo_form": photo_form})

def logout(request):
    auth.logout(request)
    return redirect("/")





def update_task(request, id):
    task = Task.objects.get(id=id)
    PhotoFormSet = inlineformset_factory(Task, Photo, form=PhotoForm, extra=1, can_delete=True)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        formset = PhotoFormSet(request.POST, request.FILES, instance=task)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("dashboard")
    else:
        form = TaskForm(instance=task)
        formset = PhotoFormSet(instance=task)
    
    return render(request, "update_task.html", {"form": form, "formset": formset, "update": True, "id": id})



def delete_task(request, id):
    print("dddd")
    print(id)
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("dashboard")
    
    
    

def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    search_query = ''
    priority = ''
    if request.GET.get('priority'):
        priority = request.GET.get('priority')
        tasks = Task.objects.filter(Q(priority=priority))
    
    
    if request.GET.get('search'):
        search_query = request.GET.get('search')
        tasks = Task.objects.filter(Q(title__icontains=search_query))
        
        print(tasks.count())
        
    return render(request, "dashboard.html", {"tasks": tasks,"search_query":search_query,"priority":priority})

    

