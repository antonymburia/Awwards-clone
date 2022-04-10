from django.shortcuts import render,redirect
from .models import Project, Profile,Rating, Comment
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
    user = request.user
    all_projects = Project.objects.filter(user = user)
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    else:
        form = UpdateProfileForm(request.POST,request.FILES)
    
    return render(request,'profile.html',{'all_projects':all_projects, 'form':form})


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
            messages.info(request,'fill all fields')
            return redirect('comment',id = project_id)

    else:
        id = id
        form = CommentForm()
        return render(request,'comment.html',{'form':form,'id':id})

@login_required(login_url = '/accounts/login/')
def project(request,id):  

    project = Project.objects.get(id = id)
    comments = Comment.objects.filter(project_id = id)
    ratings = Rating.objects.filter(project_id = id)
    designrating = []
    usabilityrating = []
    contentrating= []
    if ratings:
        for rating in ratings:
            designrating.append(rating.design)
            usabilityrating.append(rating.usability)
            contentrating.append(rating.content)

        total = len(designrating)*10
        design = round(sum(designrating)/total*100,1)
        usability = round(sum(usabilityrating)/total*100,1)
        content = round(sum(contentrating)/total*100,1)
        return render(request,'project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':content})

    else:
        design = 0
        usability = 0
        content = 0       

        return render(request,'project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':content})


@login_required(login_url = '/accounts/login/')
def rate(request,id):
    if request.method =='POST':
        ratings = Rating.objects.filter(id = id)
        for rating in ratings:
            if rating.user == request.user:
                messages.info(request,'You can only rate once')
                return redirect(project,id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')

        if design and usability and content:
            project = Project.objects.get(id = id)
            rating = Rating(design = design,usability = usability,content = content,project_id = project,user = request.user)
            rating.save()
            return redirect(project,id)

        else:
            messages.info(request,'enter required fields')
            return redirect(project,id)


    else:
        messages.info(request,'enter required fields')
        return redirect(project,id)


def logoutUser(request):
 logout(request)
 return redirect(home)



