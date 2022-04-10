from django.shortcuts import render,redirect
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UpdateProfileForm,NewProjectForm,CommentForm
from django.contrib import messages
# Create your views here.
def home(request):

    all_projects = Project.all_projects()
    return render(request,'home.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def profile(request):

    all_projects = Project.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    else:
        form = UpdateProfileForm(request.POST,request.FILES)
    return render(request,'update_profile.html',{'form':form})
@login_required(login_url = '/accounts/login/')
def new_project(request):
    if request.method=='POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect('home')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{'form':form})

@login_required(login_url = '/accounts/login/')
def comment(request,id):
    id = id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            project = Project.objects.get(id = id)
            comment.project_id = project
            comment.save()
            return redirect('home')

        else:
            project_id = id
            messages.info(request,'MAke sure you fill all the fields')
            return redirect('comment',id = project_id)

    else:
        id = id
        form = CommentForm()
        return render(request,'comment.html',{'form':form,'id':id})




def logoutUser(request):
 logout(request)
 return redirect(home)



