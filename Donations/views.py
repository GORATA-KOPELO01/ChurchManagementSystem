from django.shortcuts import render
from .models import Donation
 
def donation_history(request):
    donations = Donation.objects.all().order_by('-timestamp')
    return render(request, 'donation_history.html', {'donations': donations})
 
def donation_statistics(request):
    total_donations = Donation.objects.count()
    total_amount = Donation.objects.aggregate(models.Sum('amount'))
    average_amount = Donation.objects.aggregate(models.Avg('amount'))
    return render(request, 'donation_statistics.html', {'total_donations': total_donations, 'total_amount': total_amount, 'average_amount': average_amount})
    
# Create your views here.
