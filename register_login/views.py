from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User,auth

from register_login.decorators import unautenticated_user,allowed_users, admin_only
from.forms import UserRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from travel.models import Route_shedule


# Create your views here.

# home.............

def home(request):
    return render(request,'home.html')

# user registration in auth models.......................   
@unautenticated_user    
def register(request):
    
    form = UserRegistration()
    
    if request.method == 'POST':
        
        form = UserRegistration(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('register')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('register')
            
            else:
                user = form.save()
                user.save()
                
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                
                username = form.cleaned_data.get('username')
                messages.info(request,"Account Was Created")
                return redirect('login')
        
    context = {'form':form}
    return render(request,'register.html',context)


# user login ......
@unautenticated_user
def signin(request):
    
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user)
            return redirect('index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('login')
        
    return render(request,'login.html')

# user logout.....................
def signout(request):
    logout(request)
    return redirect('home')

# home screen diaplay.....................
@login_required(login_url='login')  
@admin_only
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def index(request): 
    return render(request,'admin.html')

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_page(request):
    
    route = Route_shedule.objects.all()
    context = {'route':route}
    return render(request,'index.html',context)


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def airport_page(request):
    return render(request,'airport.html')
