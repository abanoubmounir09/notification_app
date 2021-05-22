from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from notifications.signals import notify
from django.contrib.auth.decorators import login_required




def login_view(request):
    return render(request, 'login.html')

# def home_view(request):
#     print("******************")
#     print(request.user)
#     return render(request, 'home.html',{"user":request.user})


def index(request):
    users = User.objects.all()
    print(request.user)
    user = User.objects.get(username=request.user)
    notfs=user.notifications.unread()
    return render(request, 'home.html', {'users': users, 'user': user,'notifications':notfs})

@login_required
def message(request):
    try:
        if request.method == 'POST':
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(id=request.POST.get('user_id'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

def multimessage(request):
    try:
        if request.method == 'POST':
            sender = User.objects.get(username=request.user)
            users =request.POST.getlist('countries')
            print("******users *****",users)
            for user1 in users:
                print("******users1 *****",user1)
                receiver = User.objects.get(username=user1)
                notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

def register(request):
    if request.method == 'POST':
        print("****requset**************",request.POST)
        user=User.objects.create(username=request.POST.get('username'),password=request.POST.get('password'))
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'register.html', {})


def get_notify(request):
   user = User.objects.get(username=request.user)
   notfs=user.notifications.unread()
   for alert in notfs:
       print("notify is ",alert.actor)
   return render(request, 'brows_notific.html', {'notifications':notfs})


def mark_message_read(request,id):
    user = User.objects.get(username=request.user)
    notfs=user.notifications.unread()
    for  mesg in  notfs:
        if mesg.id == id:
            mesg.unread=0
            mesg.save()
            print("********",mesg.description)
    return HttpResponse("done")

def current_user(request):
    print("******************")
    print(request.user)
    return HttpResponse("done")



