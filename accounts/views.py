from ast import Pass
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.db.models import Sum
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from event.models import Event
from blog.models import Blog, BlogCategory
from news.models import News

from blog.models import *
from event.models import *
from main.models import *
from news.models import *



@login_required(login_url='login')
def dashboard(request):
    # Users
    userCount = User.objects.all().count()
    # Blogs
    blogPublished = Blog.objects.filter(accepted=True).count()
    # Events
    eventAll = Event.objects.all().count()
    eventOpen = Event.objects.filter(status=True).count()
    # News
    allNews = News.objects.filter(accepted=True).count()
    # Teams
    teamAll = Team.objects.filter(status=True).count()
    # Contact
    contact = Contact.objects.all().count()
    
    context = {'blogPublished':blogPublished, 'eventAll':eventAll, 'eventOpen':eventOpen, 'allNews':allNews, 'teamAll':teamAll, 'contact':contact,'userCount':userCount}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def userSection(request):
    users = Profile.objects.all()
    userCounts = users.count()
    inactveated = Profile.objects.filter(inactive=True)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        profileForm = UserProfileForm(request.POST)
        if form.is_valid() and profileForm.is_valid():
            form.save()
            profile=profileForm.save(commit=False)
            profile.user=User.objects.latest('id')
            profile.save()
            messages.success(request, 'User has been created successfully.')
            return redirect('manager')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
    form = UserRegisterForm()
    profileForm = UserProfileForm()
    context = {'form':form, 'profileForm':profileForm, 'users':users, 'userCounts':userCounts,'inactveated':inactveated}
    return render(request, 'accounts/managers.html', context)

@login_required(login_url='login')
def editUser(request, id):
    u = Profile.objects.get(id=id)
    if request.method == 'POST':
        editForm = UserUpdateForm(request.POST, instance=u.user)
        editPermission = UserProfileForm(request.POST, instance=u)
        if editForm.is_valid() and editPermission.is_valid():
            editForm.save()
            editPermission.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('manager')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
        
    editForm = UserUpdateForm(instance=u.user)
    editPermission = UserProfileForm(instance=u)

    context = {'editForm':editForm, 'editPermission':editPermission}
    return render(request, 'accounts/userEdit.html', context)

def deleteUser(request, id):
    d = Profile.objects.get(id=id)
    d.inactive = True
    d.save()
    messages.success(request, 'User has been Inactivated successfully.')
    return redirect('manager')

@login_required(login_url='login')
def eventSection(request):
    allEvents = Event.objects.all().order_by('-created')
    OngoingEvents = Event.objects.filter(status=True).count()
    PastEvents = Event.objects.filter(status=False).count()
    
    
    if request.method == 'POST':
        eventCreateForm = EventsForm(request.POST, request.FILES)
        # print(eventCreateForm.is_valid())
        if eventCreateForm.is_valid():
            eform = eventCreateForm.save(commit=False)
            eform.user = request.user
            eform.save()
            messages.success(request, 'Event was successfully Added')
            return redirect('eventSection')
        else:
            messages.error(request, 'Please correct the error below.')
    
    eventCreateForm = EventsForm()
    context = {'eventCreateForm':eventCreateForm,'allEvents':allEvents, 'OngoingEvents':OngoingEvents,'PastEvents':PastEvents}
    return render(request, 'accounts/eventSection.html', context)
  
@login_required(login_url='login')
def editEvent(request, id):
    e = Event.objects.get(id=id)
    if request.method == 'POST':
        editEventForm = EventsForm(request.POST, request.FILES, instance=e)
        if editEventForm.is_valid():
            editEventForm.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('eventSection')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
        
    editEventForm = EventsForm(instance=e)

    context = {'editEventForm':editEventForm}
    return render(request, 'accounts/eventEdit.html', context)

@login_required(login_url='login')
def blogSection(request):
    allBlogs = Blog.objects.all()
    postedBlogs = Blog.objects.filter(accepted=True).count()
    pendingBlogs = Blog.objects.filter(accepted=False).count()
    
     
    if request.method == 'POST':
        BlogCreateForm = BlogForm(request.POST, request.FILES)
        # CategoryCreationForm = BlogCategoryForm(request.POST)
        # print(BlogCreateForm.is_valid)
        # print(CategoryCreationForm.is_valid)
        if BlogCreateForm.is_valid():
            # print(CategoryCreationForm.cleaned_data)
            # CategoryCreationForm.save()
            bform = BlogCreateForm.save(commit=False)
            bform.user = request.user
            # cat = CategoryCreationForm.cleaned_data['name']
            # bform.category = cat
            # bform.category = BlogCategory.objects.latest('id')
            bform.save()
            
            
            messages.success(request, 'Post was successfully Added')
            return redirect('blogSection')
        else:
            messages.error(request, 'Please correct the error below.')
    
    BlogCreateForm = BlogForm()
    # CategoryCreationForm = BlogCategoryForm()
    context = {'BlogCreateForm':BlogCreateForm,'allBlogs':allBlogs, 'postedBlogs':postedBlogs,'pendingBlogs':pendingBlogs}
    return render(request, 'accounts/blogSection.html', context)

@login_required(login_url='login')
def editBlog(request, id):
    b = Blog.objects.get(id=id)
    if request.method == 'POST':
        editForm = EditBlogForm(request.POST, request.FILES, instance=b)
        if editForm.is_valid():
            editForm.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('blogSection')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
        
    editForm = EditBlogForm(instance=b)
    context = {'editForm':editForm}
    return render(request, 'accounts/blogEdit.html', context)

@login_required(login_url='login')
def newsSection(request):
    allNews = News.objects.all()
    filterdNews = News.objects.filter(deleted=False).order_by('-created')
    postedNews = News.objects.filter(accepted=True).count()
    pendingNews = News.objects.filter(accepted=False).count()
    
     
    if request.method == 'POST':
        NewsCreateForm = NewsForm(request.POST, request.FILES)
        if NewsCreateForm.is_valid():
            bform = NewsCreateForm.save(commit=False)
            bform.user = request.user
            bform.save()
            messages.success(request, 'Post was successfully Added')
            return redirect('NewsSection')
        else:
            messages.error(request, 'Please correct the error below.')
    
    NewsCreateForm = NewsForm()
    context = {'NewsCreateForm':NewsCreateForm,'allNews':allNews, 'postedNews':postedNews,'pendingNews':pendingNews,'filterdNews':filterdNews}
    return render(request, 'accounts/NewsSection.html', context)

@login_required(login_url='login')
def editNews(request, id):
    n = News.objects.get(id=id)
    if request.method == 'POST':
        editForm = EditNewsForm(request.POST, request.FILES, instance=n)
        if editForm.is_valid():
            editForm.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('NewsSection')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
        
    editForm = EditNewsForm(instance=n)
    context = {'editForm':editForm}
    return render(request, 'accounts/newsEdit.html', context)

@login_required(login_url='login')
def teamSection(request):
    allTeams = Team.objects.all()
    
    if request.method == 'POST':
        TeamCreateForm = TeamForm(request.POST, request.FILES)
        if TeamCreateForm.is_valid():
            tform = TeamCreateForm.save(commit=False)
            tform.user = request.user
            tform.save()
            messages.success(request, 'Member was successfully Added')
            return redirect('teamSection')
        else:
            messages.error(request, 'Please correct the error below.')
    
    TeamCreateForm = TeamForm()
    context = {'TeamCreateForm':TeamCreateForm,'allTeams':allTeams}
    return render(request, 'accounts/teamSection.html', context)

@login_required(login_url='login')
def editMember(request, id):
    t = Team.objects.get(id=id)
    if request.method == 'POST':
        editForm = EditTeamForm(request.POST, request.FILES, instance=t)
        if editForm.is_valid():
            editForm.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('teamSection')
        else:
            messages.warning(request, 'Something wrong, please check your inputs.')
        
    editForm = EditTeamForm(instance=t)
    context = {'editForm':editForm}
    return render(request, 'accounts/memberEdit.html', context)

@login_required(login_url='login')
def contactSection(request):
    allContact = Contact.objects.all().order_by('-created')
    
    context = {'allContact':allContact}
    return render(request, 'accounts/contactSection.html', context)

@login_required(login_url='login')
def contactInfos(request, id):
    c = Contact.objects.get(id=id)
    context = {'contain':c}
    return render(request, 'accounts/contactInfos.html', context)


def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You are now logged in as {username} welcome.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def userLogout(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('home')
