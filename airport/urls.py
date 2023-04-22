from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('airport_management',views.airport_management,name='airport_management'),
    path('add_airport',views.add_airport,name='add_airport'),
    path('airport_list',views.airport_list,name='airport_list'),
    path("Booking",views.Booking,name="Booking"),
    path("searchforbooking",views.searchforbooking,name="searchforbooking"),
    path("searchbooking",views.searchbooking,name="searchbooking"),
    path("BookFlight/<int:pk>",views.BookFlight,name="BookFlight"),
    path("MyBooking",views.MyBooking,name="MyBooking"),
    path("CancelBooking/<int:pk>",views.CancelBooking,name="CancelBooking"),
]
