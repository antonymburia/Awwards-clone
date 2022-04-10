from django.shortcuts import render,redirect
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UpdateProfileForm

# Create your views here.
def home(request):

    all_projects = Project.all_projects()
    return render(request,'home.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def profile(request):

    all_projects = Project.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):
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


def logoutUser(request):
 logout(request)
 return redirect(home)



