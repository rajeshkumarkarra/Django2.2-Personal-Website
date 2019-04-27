from django.db import models

# Create your models here.
# models.py is for to declare any kind of databse aspects
# mysite_client

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=5000)
    project_requirement = models.TextField()
    
    def __str__(self):
        return self.email