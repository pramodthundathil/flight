from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from register_login.decorators import allowed_users
from .forms import Route_shedule_form
from .models import Route_shedule

# Create your views here.

# search flight.................
@login_required(login_url='login')
def flightsearch(request):
    
    routes = Route_shedule.objects.all()
    context = {'routes':routes}
    
    if request.method == 'POST':
        
        flight_number = request.POST['flight_number']
        departure_date = request.POST['departure']
        
        route = Route_shedule.objects.filter(flight_number=flight_number,departure_date=departure_date)
        
        if route.exists():
            return render(request,'flight_details.html',{'route':route})
        else:
            messages.info(request,'No such Routes')
            return redirect('flightsearch')
        
    return render(request,'flightsearch.html',context)


# Flight management for admin..................
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def manage_flight(request):
    return render(request,'flights.html')

#flight Add For airport and admins..............
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_flight(request):
    
    form = Route_shedule_form()
    
    if request.method =='POST':
        
        route_number = request.POST['route_number']
        flight_number = request.POST['flight_number']
        airline_name = request.POST['airline_name']
        flight = request.POST['flight']
        departure_airport = request.POST['departure_airport']
        arrival_airport = request.POST['arrival_airport']
        departure_date =request.POST['departure_date']
        departure_time = request.POST['departure_time']
        arrival_date = request.POST['arrival_date']
        arrival_time = request.POST['arrival_time']
        
        route = Route_shedule.objects.create(route_number=route_number,flight_number=flight_number,airline_name=airline_name,flight=flight,departure_airport=departure_airport,arrival_airport=arrival_airport,departure_date=departure_date,departure_time=departure_time,arrival_date=arrival_date,arrival_time=arrival_time,flight_status="Sheduled")
        route.save()
        messages.success(request,"Route Sheduled Successfully")
        return redirect('add_flight')
        
    context = {'form':form}
    return render(request,'add_newflight_admin.html',context)

# flight add for Airport.....
@login_required(login_url='login')
def add_flight_airport(request):
    
    form = Route_shedule_form()
    
    if request.method =='POST':
              
        route_number = request.POST['route_number']
        flight_number = request.POST['flight_number']
        airline_name = request.POST['airline_name']
        flight = request.POST['flight']
        departure_airport = request.POST['departure_airport']
        arrival_airport = request.POST['arrival_airport']
        departure_date =request.POST['departure_date']
        departure_time = request.POST['departure_time']
        arrival_date = request.POST['arrival_date']
        arrival_time = request.POST['arrival_time']
        
        route = Route_shedule.objects.create(route_number=route_number,flight_number=flight_number,airline_name=airline_name,flight=flight,departure_airport=departure_airport,arrival_airport=arrival_airport,departure_date=departure_date,departure_time=departure_time,arrival_date=arrival_date,arrival_time=arrival_time,flight_status="Sheduled",user = request.user)
        route.save()
        messages.success(request,"Route Sheduled Successfully")
        return redirect('add_flight_airport')
    
    context = {'form':form}
    return render(request,'add_newflight_airport.html',context)

#flight management for airport
@login_required(login_url='login')
def manage_flight_airport(request):
    return render(request,'flights_airport.html')

# shedule Update
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def sheduled_route_update_admin(request):
    
    all_routes = Route_shedule.objects.all()
    
    context= {'all_routes':all_routes}
    
    return render(request,'sheduled_route_update_admin.html',context)


#airport route reshedule
@login_required(login_url='login')
def sheduled_route_update_airport(request):
    all_routes = Route_shedule.objects.all()
    
    context= {'all_routes':all_routes}
    
    return render(request,'shedule_routes_airport.html',context)

#reshedule admin...
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def reshedule_flight(request):
    
    serial_number = request.POST['submit']
    route = Route_shedule.objects.filter(serial_number = serial_number)        
    
    all_routes = Route_shedule.objects.all()
    
    context = {'route':route,'all_routes':all_routes}
    return render(request,'resheduled_flight.html',context)

# flight reshedule airport....
@login_required(login_url='login')
def reshedule_flight_airport(request):
    serial_number = request.POST['submit']
    route = Route_shedule.objects.filter(serial_number = serial_number)        
    
    all_routes = Route_shedule.objects.all()
    
    context = {'route':route,'all_routes':all_routes}
    return render(request,'resheduled_flight_airport.html',context)
    
    

# resheduling flight admin....
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_reshedule_flight(request):
    
    serial_number = request.POST['s_no']
    route = Route_shedule.objects.get(serial_number = serial_number)
    
    
    route.route_number = request.POST['route_number']
    route.flight_number = request.POST['flight_number']
    route.airline_name = request.POST['airline_name']
    route.flight = request.POST['flight']
    route.departure_airport = request.POST['departure_airport']
    route.arrival_airport = request.POST['arrival_airport']
    route.departure_date =request.POST['departure_date']
    route.departure_time = request.POST['departure_time']
    route.arrival_date = request.POST['arrival_date']
    route.arrival_time = request.POST['arrival_time']
    route.flight_status = 'RESHEDULED'
    route.flight_delay = request.POST['flight_delay']
    
    route.save()
    messages.success(request,'Flight was resheduled')
    return redirect('sheduled_route_update_admin')

#resheduling flight Airport.......
@login_required(login_url='login')
def update_reshedule_flight_airport(request):
    
    serial_number = request.POST['s_no']
    route = Route_shedule.objects.get(serial_number = serial_number)
    
    
    route.route_number = request.POST['route_number']
    route.flight_number = request.POST['flight_number']
    route.airline_name = request.POST['airline_name']
    route.flight = request.POST['flight']
    route.departure_airport = request.POST['departure_airport']
    route.arrival_airport = request.POST['arrival_airport']
    route.departure_date =request.POST['departure_date']
    route.departure_time = request.POST['departure_time']
    route.arrival_date = request.POST['arrival_date']
    route.arrival_time = request.POST['arrival_time']
    route.flight_status = 'RESHEDULED'
    route.flight_delay = request.POST['flight_delay']
    
    route.save()
    messages.success(request,'Flight was resheduled')
    return redirect('sheduled_route_update_airport')
    