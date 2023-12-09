from django.db import models

# Create your models here.
class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    course=models.CharField(max_length=255, choices=[('Mca', 'Mca'),('B.E/B.tech', 'B.E/B.tech'),('Bca', 'Bca'),('Bsc', 'Bsc'),('B.com', 'B.com'),('Diploma', 'Diploma'),('ITI', 'ITI'),])
    gender=models.CharField(max_length=255,choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    department=models.CharField(max_length=255,choices=[('CS','CS'),('IT','IT'),('EC','EC')])
    college_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.full_name} - {self.course}"

    class Meta:
        app_label = 'registration_app'  # Specify your app label here
