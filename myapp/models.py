from django.db import models

# Create your models

class time(models.Model):
    title=models.CharField(max_length=10)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(auto_now_add=True)
    mail_id=models.EmailField(unique=True,null=True)



class Event(models.Model):
    title=models.CharField(max_length=100)
class Participant(models.Model):
    Name=models.CharField(max_length=100)
    Email_id=models.EmailField(unique=True)
    Registration_date=models.DateTimeField(auto_now_add=True)
    Event=models.ForeignKey(Event,on_delete=models.CASCADE)

class JobPosition(models.Model):
    title=models.CharField(max_length=100)
class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Mail_id=models.EmailField(unique=True,null=True)
    Salary=models.IntegerField(null=True)
    JobPosition=models.OneToOneField(JobPosition,on_delete=models.CASCADE)

class Event(models.Model):
    title=models.CharField(max_length=100)
class Participant(models.Model):
    Name=models.CharField(max_length=100)
    Email_id=models.EmailField(unique=True)
    Registration_date=models.DateTimeField(auto_now_add=True)
    Event=models.ForeignKey(Event,on_delete=models.CASCADE)