from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.http import HttpResponseRedirect , HttpResponse 
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import task
from .models import signupform

# class TaskList(ListView):
#     model = task
#     context_object_name = 'tasks'
#     template_name = 'base/main.html'
# Create your views here.

# class TaskDetail(DetailView):
#     model = task
#     context_object_name = 'task'
#     template_name = 'base/detail.html'
    
# class TaskCreate(CreateView):
#     model = task
#     fields = '__all__'
#     success_url= reverse_lazy()
    
# making it self

def TaskList(request):
    return render(request, 'base/main.html')

def TaskList(request):
    all_todo_items = task.objects.all() 
    return render(request, 'base/main.html',
    {'all_items':all_todo_items}) 
    
def TaskDetail(request, id):
     # rendaring page
    obj = task.objects.get(id=id)
    mydictionary = {
    "tittle" : obj.tittle,
    "description" : obj.description,
    "status" : obj.complete,
    "create" : obj.create
    
    }
    return render(request,'base/detail.html',context=(mydictionary))

def CreateTask(request):
    return render(request, 'base/task_form.html')

def SaveTask(request):
    if request.method=="POST":
        tittle = request.POST.get('tittle')
        description = request.POST.get('description')
        # complete = request.POST.get('complete')
        data = task(tittle=tittle, description=description )
        
        data.save()
        
        # if complete== 'on':
        #     complete =True
        # else:
        #     complete = False
    return HttpResponseRedirect(reverse('hometasks'))

def DeleteTask(request, id):
    y = task.objects.get(id= id)
    y.delete()
    return HttpResponseRedirect(reverse('hometasks'))

def edit(request, id):
    # rendaring page
    obj = task.objects.get(id=id)
    mydictionary = {
    "tittle" : obj.tittle,
    "description" : obj.description,
    "id" : obj.id
    
    }
    return render(request,'base/edit.html',context=(mydictionary))

def update(request,id):    
    tittle = request.POST['newtittle']
    description = request.POST['newdescription']
    x = task.objects.get(id=id)
    x.tittle = tittle
    x.description = description
    # el = data(tittle = tittle, description = description,)
    x.save()
    
    return HttpResponseRedirect(reverse('hometasks'))
    
def SignUpView(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save
            return redirect('login')
    else:
        form = signupform()
    return render(request, 'base/signup.html', {'form' : form})

def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request.user)
            return render('next')
    else:
        return render(request, 'base/login.html')
    
# def next(request):
#     return render(request, '')