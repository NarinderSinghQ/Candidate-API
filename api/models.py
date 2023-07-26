from django.db import models

# Create your models here.


class Candidate(models.Model):
    Name = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=20, unique=True) 
    Email = models.CharField(max_length=40)
    def __str__(self):
        return self.Name
    
    
class Callhistory(models.Model):
    Candidate = models.ForeignKey(Candidate , on_delete= models.CASCADE , related_name= "Candidate")
    Date = models.DateTimeField(auto_now_add=True)
    # call_recording = models.FileField(upload_to='call_recordings/' , null= True , default= None) 
    Call_time = models.DurationField(null=True)
    def __str__(self):
        return self.Candidate.Name
    
