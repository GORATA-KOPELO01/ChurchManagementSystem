from django.urls import path
from . import views 

app_name = 'Events' 

urlpatterns = [     
    path('', views.event_list, name='event_list'),    
     path('<int:event_id>/', views.event_detail, name='event_detail'),     
     path('create/', views.event_create, name='event_create'),     
     path('<int:event_id>/update/', views.event_update, name='event_update'),     
     path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
      ]
