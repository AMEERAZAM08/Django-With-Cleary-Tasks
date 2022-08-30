"""hq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#view 
from  dummyapp import views

from django.urls import path,include
from  django.conf.urls import url
 

from  dummyapp.views import UsersListView
from  dummyapp.views import GenerateRandomUserView


# from Django.hq import dummyapp

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    url('users/', UsersListView.as_view(), name='users_list'),
    url('generate/', GenerateRandomUserView.as_view(), name='generate'),
    path('add/',views.add),
    path('insert/',views.insert),
    path('show/',views.show),
    path('show_by_id/',views.show_by_age),
    # about 
    url(r'^about/$',views.about,name='about'),
    url(r'^homepage/$',views.homepage,name='homepage'),
    url('predict/',views.predict_model),
    
 
]
