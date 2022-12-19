

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserCreationForm,ProfileForm
from .models import User,Profile
from . serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required


# ------------------------------------------------------------------------------------------------------|
#                                                                                   
#   REGISTRATION AND USER MANAGEMENT
# ------------------------------------------------------------------------------------------------------|
@login_required(login_url="login")
def profile(request):
   profile = request.user.profile
   context={'profile':profile}
   return render(request,'user/profile.html',context)


def update_profile(request):
    profile  = request.user.profile

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('profile')
        else:
            messages.error(request,'There is an error while processing your in put')
    context = {'form':form}
    return render(request, 'user/new.html',context)


def register(request):
    if request.user.is_authenticated:
         return redirect('index')
    form = NewUserCreationForm()
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'user/register.html', context)
    context = {"form":form}
    return render(request, 'user/register.html', context)



def login_page(request):
    if request.user.is_authenticated:
         return redirect('index')
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        try:
            user = User.objects.get(phone_number = phone_number)
        except:
            messages.error(request, 'User with this phone number does not exist ')
        user = authenticate(request, phone_number = phone_number, password=password)
        if user is not None:
            login(request, user)
            ## come changes made to allow user go back to where he left before logging in
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        else:
            messages.error(request, 'Your password is not correct')
    return render(request, 'user/login.html')


# logout
def logout_page(request):
    logout(request)
    return redirect('index')




@api_view(['GET'])
def profile(request):
    profile = Profile.objects.all()
    profile_data = ProfileSerializer(profile,many=True)
    return Response(profile_data.data)