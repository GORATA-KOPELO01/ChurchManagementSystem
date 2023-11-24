from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import Staff, Member, Message

def send_message(request):
    if request.method == 'POST':
        sender_id = request.POST.get('sender_id')
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')

        sender = Staff.objects.get(id=sender_id)
        receiver = Member.objects.get(id=receiver_id)

        message = Message(sender=sender, receiver=receiver, content=content)
        message.save()

        # Send email
        send_mail(
            'New Message',
            content,
            settings.EMAIL_HOST_USER,
            [receiver.email],
            fail_silently=False,
        )

        # Send SMS
        # Code to send SMS goes here

        # Send letter
        # Code to send letter goes here

        return render(request, 'success.html')

    staff = Staff.objects.all()
    members = Member.objects.all()

    return render(request, 'send_message.html', {'staff': staff, 'members': members})
# Create your views here.
