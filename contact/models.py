from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    massage = models.TextField()
    
    def __str__(self):
        return self.name