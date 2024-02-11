from django.shortcuts import render

from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import TaskForm,LoginForm,PhotoForm
from django.shortcuts import redirect
from django.contrib.auth.models import auth

from .models import Task,Photo
# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    return HttpResponse("This is the register page")


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
        if form.is_valid():
            form.save()
            return redirect("dashboard/")
    else:
        form = TaskForm()
    return render(request, "create_task.html", {"form": form})


# def update_task(request,id):
#     task = Task.objects.get(id=id)
#     photo = Photo.objects.filter(task=task)
#     print(task)
#     form = TaskForm(instance=task)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard/")
#     return render(request, "update_task.html", {"form": form,"update":True,"photo":photo})
    

def update_task(request, id):
    task = Task.objects.get(id=id)
    photos = Photo.objects.filter(task=task)

    # Initialize the TaskForm with the task instance
    task_form = TaskForm(instance=task)

    # Create a formset for the Photo model
    PhotoFormSet = inlineformset_factory(Task, Photo, form=PhotoForm, extra=1, can_delete=True)
    photo_formset = PhotoFormSet(instance=task)

    if request.method == "POST":
        # Populate the forms with the POST data and instance
        task_form = TaskForm(request.POST, instance=task)
        photo_formset = PhotoFormSet(request.POST, request.FILES, instance=task)

        if task_form.is_valid() and photo_formset.is_valid():
            task_form.save()  # Save the task details
            photo_formset.save()  # Save the photo details
            return redirect("dashboard")  # Redirect after successful update

    # Render the template with the forms and photos
    return render(request, "update_task.html", {"task_form": task_form, "photo_formset": photo_formset, "update": True})




def delete_task(request):
    return HttpResponse("This is the delete page")

def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"tasks": tasks})

    

