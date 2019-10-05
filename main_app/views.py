from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment
from .models import User
from .models import Taken
#from .models import Chat
from .import views

def HomeView(request):
    if request.method == "POST":
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2= request.POST['password2']

        apply = User(username=username,email=email,password=password,password2=password2)
        #apply2 = Chat(message=message)
        apply.save()
        #apply2.save()
        return render(request,'index.html')
    else:
        return render(request, 'index.html')

def Index2(request):
    return render(request, 'index2.html')

def Index3(request):
    if request.POST == "POST":
        username= request.POST['username']
        week = request.POST['week']
        email = request.POST['email']
        app = Taken(username=username,week=week,email=email)
        app.save()
        return render(request,'index6.html')
    else:
     return render(request, 'index3.html')

def Index4(request):
    return render(request, 'index4.html')

def Index5(request):
    return render(request, 'index5.html')

def Index6(request):
    return render(request, 'index6.html')

def Index7(request):
    if request.method == "POST":
        username= request.POST['username']
        email = request.POST['email']
        time = request.POST['time']


        apply = Appointment(username=username,email=email,time=time)
        apply.save()

        return render(request,'index7.html')
    else:
        return render(request, 'index7.html')

def list(request):
    post = Appointment.objects.all()
    context = {
        "post": post
    }
    return render(request,'list.html',context)


