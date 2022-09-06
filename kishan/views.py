from multiprocessing import context
from django.template import RequestContext
# from setuptools import required
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from.forms import usersRegisterForm
from datetime import datetime
from kishan.models import Contact
from kishan.models import Register
from kishan.models import Schemes
from django.contrib import messages

# Create your views here.
# def index(request):
#     return HttpResponse("this is subhasis")
def home(request):
    return render(request,'templates/home.html')

def benifit(request):    
    return render(request,'templates/benifit.html')
def scheme(request): 
    schemeData=Schemes.objects.all()
    # for a in schemeData:
    #     print(a.scheme_icon)
    # print(scheme)
    data={
        'schemeData':schemeData
    }
    return render(request,'templates/scheme.html')
def dashbord(request):    
    return render(request,'templates/dashbord.html')
def FAQ(request):    
    return render(request,'templates/FAQ.html')
def login(request):    
    return render(request,'templates/login.html')
def loginhome(request):    
    return render(request,'templates/loginhome.html')
def userinput(request):    
    return render(request,'templates/userinput.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
    messages.success(request, f'Your message sucessfully sent.')
    return render(request,'contact.html')


# def register(request):    
#     if request.method == 'POST':
#         form = Register(request.POST)
#         if form.is_valid():
#             form.save()
#             fname = form.cleaned_data.get('username')
#             fname = request.POST.get('fname')
#             lname = request.POST.get('lname')
#             email = request.POST.get('email')
#             number = request.POST.get('number')
#             address = request.POST.get('address')
#         # password = request.POST.get('password')
#         register = Register(fname=fname,lname=lname, email=email, number=number, address=address, date=datetime.today())
#         register.save()
#         messages.success(request, 'Your Request was sucessfully sent.')
#         return render(request,'register.html')
#     else:
#         form = Register()
#         return render(request,'register.html',{'form':form})

def register(request):    
    if request.method == 'POST':           
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        number = request.POST.get('number')        
        message = request.POST.get('message')
        register = Register(fname=fname,lname=lname, email=email, number=number,message=message , date=datetime.today())
        register.save()
        messages.success(request, 'Your Request was sucessfully sent.')
    return render(request,'templates/register.html')

        #     from.save()
        #     username = form.cleand_data.get('username')
        #     messages.success(request, f'Congratulations ! Account has been created.')
        #     return('login')
        # else{
        #     form = UserRegisterForm()
        # }
            
        
 