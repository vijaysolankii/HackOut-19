from django.db import models

class User(models.Model):
    username = models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250,default="")
    password = models.CharField(max_length=250,default="")
    password2 = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.username



class Consultant(models.Model):
    c_id = models.IntegerField()
    c_name = models.CharField(max_length=250,default="")
    designition = models.CharField(max_length=250,default="")
    hospital_name = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.c_name




class Taken(models.Model):
    username= models.CharField(max_length=250,default="")
    week = models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250,default="")
    def __str__(self):
        return self.username



class Chat(models.Model):
    c_id = models.ForeignKey(Consultant,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=250,default="")
    def __str__(self):
        return self.username



class Appointment(models.Model):
    username = models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250,default="")
    time = models.CharField(max_length=250,default="")
    def __str__(self):
        return self.username

