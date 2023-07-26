from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40 )
#vaidations??
    def __str__(self):
        return self.name


class Callhistory(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="Candidate"
    )
    date_time = models.DateTimeField(auto_now_add=True)
    # call_recording = models.FileField(upload_to='call_recordings/' , null= True , default= None)
    call_Duration = models.DurationField(null=True)

    def __str__(self):
        return self.candidate.name
