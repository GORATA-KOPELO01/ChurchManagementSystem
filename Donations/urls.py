from django.urls import path
from . import views

urlpatterns = [
    path('donation/history/', views.donation_history, name='donation_history'),
    path('donation/statistics/', views.donation_statistics, name='donation_statistics'),
]