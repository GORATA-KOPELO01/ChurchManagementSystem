from django.contrib import admin
from .models import Staff, Member, Message


# Register your models here.
admin.site.register(Staff)
admin.site.register(Member)
admin.site.register(Message)