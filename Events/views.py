
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event

def event_list(request):     
    events = Event.objects.all()     
    return render(request, 'events/event_list.html', {'events': events}) 

def event_detail(request, event_id):    
        event = get_object_or_404(Event, pk=event_id)    
        return render(request, 'events/event_detail.html', {'event': event}) 

def event_create(request):    
    if request.method == 'POST':         
                #Handle form submission        
         pass    
    else:         
                # Display empty form        
                pass

def event_update(request, event_id):     
    event = get_object_or_404(Event, pk=event_id)     
    if request.method == 'POST':        
        # Handle form submission       
        pass    
    else:         
        # Display pre-filled form        
        pass

def event_delete(request, event_id):     
    event = get_object_or_404(Event, pk=event_id)     
    if request.method == 'POST':         
        # Handle event deletion       
        pass    
    else:        
         # Display confirmation page       
          pass


  

