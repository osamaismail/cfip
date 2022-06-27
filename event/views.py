from django.shortcuts import render, redirect
from .models import Attend, Event
import datetime
from .forms import AttendForm, CaptchaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.timezone import localtime
import pytz



def eventList(request):
    allEvents = Event.objects.all().order_by('-created')
    p = Paginator(allEvents, 6)
    page = request.GET.get('page')
    events = p.get_page(page)
    
    context = {'events':events, 'allEvents':allEvents}
    return render(request, 'event/events.html', context)





def event(request, id):
    detail = Event.objects.get(id=id)
    today = datetime.datetime.now(pytz.timezone('Asia/Baghdad')).date()
    print(detail.eventDate)
    print(type(detail.eventDate))
    # evenDate = localtime(detail.eventDate)
    evenDate = detail.eventDate
    Timecheck = evenDate > today

    if not Timecheck:
        detail.status = False
    else:
        detail.status = True
    detail.save()
        
    if request.method == 'POST':
        FormAttend = AttendForm(request.POST)
        cform = CaptchaForm(request.POST)
        IDLis = []
        if FormAttend.is_valid() and cform.is_valid():
            getEmail = FormAttend.cleaned_data['email']
            emailCheck = Attend.objects.filter(email=getEmail).values_list('event')
            
            for i in emailCheck:
                IDLis.append(i[0])
            if detail.id not in IDLis:
                human = True
                newAttend = FormAttend.save(commit=False)
                newAttend.event = detail
                newAttend.save()
                messages.success(request,'Thanks, you have been subscribed to this event')
                return redirect('event', id=detail.id)
            else:
                messages.warning(request,'Sorry, this email in already subscribed to this event')
                FormAttend = AttendForm()
                cform = CaptchaForm()
    else:   
        FormAttend = AttendForm()
        cform = CaptchaForm()
    context = {'detail':detail,'FormAttend':FormAttend,'cform':cform, 'Timecheck':Timecheck}
    return render(request, 'event/event.html', context)

            