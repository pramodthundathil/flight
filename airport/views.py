from django.contrib import messages
from django.shortcuts import render,redirect
import airport
from register_login.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from travel.models import Route_shedule
from register_login.forms import UserRegistration
from travel.forms import BookingForm
from travel.models import Bookings
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest

razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# Create your views here.
# manage airport views...........
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def airport_management(request):
    return render(request,'airport_management.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_airport(request):
    
    form = UserRegistration()
    
    if request.method== "POST":
        
        form = UserRegistration(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('add_airport')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('add_airport')
            
            else:
                airport = form.save()
                airport.save()
                
                group = Group.objects.get(name='airport')
                airport.groups.add(group)
                
                username = form.cleaned_data.get('username')
                messages.info(request,"Account Was Created")
                return redirect('add_airport')     
    
    context = {'form':form}
    
    return render(request,'add_airport.html',context)

# list airport
def airport_list(request):
    
    airports = User.objects.filter(groups__name__in=['airport'])
    context = {'airport':airports}
    
    return render(request,'airports/airport_list.html',context)

def Booking(request):
    return render(request,"bookings.html")

def searchforbooking(request):
    return render(request,"serchforbooking.html")

def searchbooking(request):
    if request.method == "POST":
        search = request.POST["search"]
        products = Route_shedule.objects.filter(arrival_airport__contains = search)
        
        return render(request, "search.html",{"search":search,"products":products})
    
    return redirect("searchforbooking")

def BookFlight(request,pk):
    form  = BookingForm()
    val = Route_shedule.objects.get(serial_number = pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.user = request.user
            data.filght = val
            data.save()
            messages.info(request,"Booking Confirmed")
            return redirect("Makepayment")
    
    context = {
        "val":val,
        "form":form
    }
    return render(request,"bookingconfirmation.html",context)

def Makepayment(request):
    currency = 'INR'
    amount = 1000 * 100 # Rs. 200
    context = {}

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = "http://127.0.0.1:8000/airportSuccess"

  # we need to pass these details to frontend.
    
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = "1",
    
    return render(request,"Makepayment.html",context)

@csrf_exempt
def Success(request):
    messages.info(request,"Booking Confirmed")
    return redirect("index")

def MyBooking(request):
    Booking = Bookings.objects.filter(user = request.user)
    context = {
        "Booking":Booking
    }
    return render(request,"mybookings.html",context)

def CancelBooking(request,pk):
    Bookings.objects.get(id = pk).delete()
    messages.info(request,"Booking Cancelled")
    return redirect('index')