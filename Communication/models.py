from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Message(models.Model):
    sender = models.ForeignKey(Staff, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

# Create your models here.
