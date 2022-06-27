from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Team
from django.db.models import Q
from blog.models import Blog
from event.models import Event
from news.models import News







def search(request):
    searched = request.GET.get('search')
    qsb = Blog.objects.filter(Q(title__icontains=searched)|Q(content__icontains=searched)).distinct()
    qse = Event.objects.filter(Q(title__icontains=searched)|Q(content__icontains=searched)).distinct()
    qsn = News.objects.filter(Q(title__icontains=searched)|Q(content__icontains=searched)).distinct()
    
    context={'searched':searched,'qsb':qsb,'qse':qse,'qsn':qsn}
    return render(request,'main/search.html', context)




def index(request):
    return render(request, 'main/index.html')


def team(request):
    AllTeam = Team.objects.filter(status=True).order_by('-created')
    context = {'AllTeam':AllTeam}
    return render(request, 'main/team.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for your message, it will be answered as soon as possible')
            return redirect('contact_us')
        else:
            messages.warning(request,'Something wrong with email or phone number please checked it')
    else:
        form = ContactForm()
    
    context = {'form':form}
    return render(request, 'main/contact.html', context)
