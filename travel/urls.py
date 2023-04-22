from django.urls import path
from.import views

urlpatterns = [
    path('flightsearch',views.flightsearch,name='flightsearch'),
    path('manage_flight',views.manage_flight,name='manage_flight'),
    path('manage_flight_airport',views.manage_flight_airport,name = 'manage_flight_airport'),
    
    path('add_flight',views.add_flight,name='add_flight'),
    path('add_flight_airport',views.add_flight_airport,name = "add_flight_airport"),
    path('sheduled_route_update_admin',views.sheduled_route_update_admin,name = 'sheduled_route_update_admin'),
    path('reshedule_flight',views.reshedule_flight,name ='reshedule_flight'),
    path('update_reshedule_flight',views.update_reshedule_flight,name='update_reshedule_flight'),
    
    path('sheduled_route_update_airport',views.sheduled_route_update_airport,name = 'sheduled_route_update_airport'),
    path('reshedule_flight_airport',views.reshedule_flight_airport,name = 'reshedule_flight_airport'),
    path('update_reshedule_flight_airport',views.update_reshedule_flight_airport,name='update_reshedule_flight_airport')
]
