
from django.contrib import admin
from django.urls import path, include
from kishan import views
urlpatterns = [

    # path('admin/', admin.site.urls),
    # path("",views.index,name='kishan'),
    path("",views.home,name='home'),
    path("benifit/",views.benifit,name='benifit'),
    path("scheme/",views.scheme,name='scheme'),
    path("dashbord/",views.dashbord,name='dashbord'),
    path("FAQ/",views.FAQ,name='FAQ'),
    # path("services",views.services,name='services'),
    path("contact/",views.contact,name='contact'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("loginhome/",views.loginhome,name='loginhome'),
    path("userinput/",views.userinput,name='userinput'),

]
    
