"""cfipage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from event.views import eventList, event
from news.views import *
from blog.views import *
from accounts.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('captcha/', include('captcha.urls')),
    # index
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_us'),
    path('ourTeam/', views.team, name='team'),
    # Search
    path('searching/', views.search, name='search'),
    # events
    path('events/', eventList, name='eventList'),
    path('event/<id>/', event, name='event'),
    # news
    path('news/', allNews, name='allNews'),
    path('news/<id>/', news, name='news'),
    # path('category/<id>/', category, name="category"),
    # blog
    path('blogs/', allBlogs, name='blogs'),
    path('blog/<id>/', blog, name='blog'),
    # Accounts
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
    path('managers/', userSection, name='manager'),
    path('manage/<id>', editUser, name='edit'),
    path('inactive/<id>', deleteUser, name='inactivate'),
    # path('manage/changePassword/<id>', editUser, name='changePassword'),
    
    path('eventsManage/', eventSection, name='eventSection'),
    path('events/<id>', editEvent, name='editEvent'),
    
    path('blogsManage/', blogSection, name='blogSection'),
    path('blogs/<id>', editBlog, name='editBlog'),
    
    path('NewsManage/', newsSection, name='NewsSection'),
    path('Newss/<id>', editNews, name='editNews'),
    
    path('TeamManage/', teamSection, name='teamSection'),
    path('member/<id>', editMember, name='editMember'),
    
    path('contactManage/', contactSection, name='contactSection'),
    path('contactInfo/<id>', contactInfos, name='showContact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
