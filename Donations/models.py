from django.db import models
 
class Donation(models.Model):
    DONATION_TYPES = (
        ('T', 'Tithes'),
        ('O', 'Other Givings'),
    )
 
    donation_type = models.CharField(max_length=1, choices=DONATION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.get_donation_type_display()} - {self.amount}"

# Create your models here.
