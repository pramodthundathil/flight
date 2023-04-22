from django.db import models



# Create your models here.
class Enquery(models.Model):
    
    serial_number = models.AutoField(primary_key=True)
    enquery_airport = models.CharField(max_length=100)
    enquery_subject = models.CharField(max_length=200)
    enquery_enquery = models.CharField(max_length=1000)
    enquery_date = models.DateTimeField(auto_now_add=True)
    enquery_answer =models.CharField(max_length=1000,null=True)
    answer_date = models.DateTimeField(auto_now_add=False,null=True)
    referrences = models.CharField(max_length=100,null=True)