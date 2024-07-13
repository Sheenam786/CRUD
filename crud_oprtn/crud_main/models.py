from django.db import models


class contactform(models.Model):
    name = models.CharField(max_length=100, default=True, blank=True)
    email = models.EmailField()
    number = models.IntegerField()
    date = models.DateField(max_length=15)


    def __str__(self):
        return self.name
    

class Register(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    passwrd = models.CharField(max_length=100)


    def __str__(self):
        return self.name