
from django.shortcuts import render, redirect, HttpResponse
from Authentication.forms import UpdateUserForm, CreationUserForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Member
 
 
def createuser(request):
    form = CreationUserForm()
    if request.method == 'POST':
        form= CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
           
 
            return redirect('add_member')
    context = {'form':form}
    return render(request,'add_member.html',context)
 
 
def update_user(request, user_id):
    user_instance = User.objects.get(pk=user_id)
 
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user_instance)
 
        if user_form.is_valid():
            user_form.save()
 
            
            return redirect('update_user', user_id=user_id)  
    else:
        user_form = UpdateUserForm(instance=user_instance)
 
    return render(request, 'update_member.html', {
        'user_form': user_form,
    })
 
def member_list(request):
    users = User.objects.all()
    return render(request,'member_list.html',{'users':users})
 
 
def deleteUser(request,pk):
    account = User.objects.get(id=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('member_list')
 
    context={'account':account}
    return render(request,"delete_member.html",context)
 
 
def upcoming_birthdays(request):
    current_date = timezone.now().date()
 
    upcoming_birthdays = Member.objects.filter(birthdate__gt=current_date).order_by('birthdate')[:5]
 
    return render(request, "upcoming_bday.html", {"upcoming_birthdays": upcoming_birthdays})
 

 

# Create your views here.
