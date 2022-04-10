from django.shortcuts import render
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
# Create your views here.
def home(request):

    all_projects = Project.all_projects()
    return render(request,'home.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def profile(request):

    all_projects = Project.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_projects':all_projects})



def logoutUser(request):
 logout(request)
 return redirect(home)



