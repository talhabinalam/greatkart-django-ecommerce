from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name