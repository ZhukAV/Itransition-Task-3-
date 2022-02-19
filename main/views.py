from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model


def registerPage(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('registerPage')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('registerPage')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return redirect('mainPage')
        else:
            messages.info(request,'Password do not match')
            return redirect('registerPage')
    else:
        return render(request, 'main/register.html')

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('mainPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username',False)
            password = request.POST.get('password',False)

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('mainPage')
            else:
                messages.info(request,'invalid credentials')
                return redirect('loginPage')
        else:
            return render(request, 'main/login.html')

def logout(request):
    auth.logout((request))
    return redirect('loginPage')

def mainPage(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'main/main.html',{'users':users})

def edit(request):
    if request.method == 'POST' and 'delete' in request.POST:
        ID = request.POST.getlist('ID')
        for values in ID:
            user = User.objects.get(id=values)
            user.delete()
        return redirect('loginPage')
    elif request.method == 'POST' and 'block' in request.POST:
        ID = request.POST.getlist('ID')
        for values in ID:
            user = User.objects.get(id=values)
            user.is_active = False
            user.save()
            if request.user.username == user.username:
                auth.logout((request))
        return redirect('loginPage')
    elif request.method == 'POST' and 'unblock' in request.POST:
        ID = request.POST.getlist('ID')
        for values in ID:
            user = User.objects.get(id=values)
            user.is_active = True
            user.save()
        return redirect('mainPage')
    else:
        return redirect('mainPage')



