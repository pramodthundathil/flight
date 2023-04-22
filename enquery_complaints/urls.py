from django.urls import path
from.import views

urlpatterns = [
    path('enquery',views.enquery,name= 'enquery'),
    path('replay_enquery_admin',views.replay_enquery_admin,name = 'replay_enquery_admin'),
    path('delete_enquery_admin',views.delete_enquery_admin,name = 'delete_enquery_admin'),
    path('repaly_to_enquery_admin',views.repaly_to_enquery_admin,name = 'repaly_to_enquery_admin'),
    path('replay',views.replay,name='replay'),
    path('messages_for_customer',views.messages_for_customer,name='messages_for_customer')
]
