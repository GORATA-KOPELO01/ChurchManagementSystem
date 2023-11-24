from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory




from django.contrib.auth import authenticate, login,logout


from django.contrib import messages


from django.contrib.auth.decorators  import login_required
from django.views import View

# Create your views here.
from .models import *
from .forms import CreationUserForm


def signupPage(request):
    if request.user.is_authenticated:
        return  redirect('home')
    else:
            form = CreationUserForm()
            if request.method == 'POST':
                form= CreationUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    
                    messages.success(request,'Account was created successfully')

                    return redirect('login')
            context = {'form':form}
            return render(request,'signup.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return  redirect('home')
    
    else:
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request,user)
                    return redirect('home')
        
                else:
                     messages.info(request, 'Username or password is incorrect')
                    
            context = {}
            return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):

    return render(request,'home.html')




# Create your views here.
