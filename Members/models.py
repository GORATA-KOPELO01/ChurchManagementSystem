from django.db import models
from django.contrib.auth.models import User
 
 
class Member(models.Model):
    CATEGORY_CHOICES = (
        ('Adult', 'Adult'),
        ('Teen', 'Teen'),
        ('Sunday School', 'Sunday School'),
        ('Visitor', 'Visitor'),
    )
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    email = models.EmailField()
    

# Create your models here.
