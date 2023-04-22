from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Enquery
from datetime import datetime
# Create your views here.

def enquery(request):
    
    if request.method == "POST":
        
        subject = request.POST['subject']
        airport = request.POST['airport']
        enquery_1 = request.POST['enquery']
        user = request.user.username
        
        customer_enquery = Enquery.objects.create(enquery_airport = airport, enquery_subject = subject,enquery_enquery = enquery_1,referrences = user)
        customer_enquery.save()
        
        messages.info(request,'Enquery sent')
        return redirect('enquery')
        
    return render(request,'enquery/enquery_customer.html')

# admin replay to enqueryies........................
def replay_enquery_admin(request):
    
    enqueries = Enquery.objects.all()
    context = {'enqueries': enqueries}
    
    return render(request,'enquery/enquery_view_admin.html',context)

def delete_enquery_admin(request):
    
    serial_number = request.POST['delete']
    
    enqu = Enquery.objects.get(serial_number = serial_number)
    enqu.delete()
    messages.success(request,'Enquery deleted')
    return redirect('replay_enquery_admin')

def repaly_to_enquery_admin(request):
    
    serial_number = request.POST['replay']
    enqu = Enquery.objects.filter(serial_number = serial_number)
      
    context = {'enquery':enqu}
    
    return render(request,'enquery/replay_enquery_admin.html',context)

def replay(request):
    
    serial_number = request.POST['replay_no']
    enqu = Enquery.objects.get(serial_number = serial_number)
    enqu.enquery_answer = request.POST['replay_to']
    enqu.answer_date = datetime.now()
    enqu.save()
    
    messages.success(request,'Message Sent')
    return redirect('replay_enquery_admin')

# replayed enquery view for customers.................................
def messages_for_customer(request):
    
    user = request.user.username
    message = Enquery.objects.filter(referrences = user)
    
    context = {'message': message}
    
    return render(request,'enquery/messages.html',context)
     

    


