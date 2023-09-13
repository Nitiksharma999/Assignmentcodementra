from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    data = Blog.objects.all()
    return render (request,'home.html',{'data':data})


def addblog(request):
    if request.method == 'GET':
        form = blogform()
        return render(request,'addblog.html',{'form':form})
    else:
        form = blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addblog')
        else:
            return render(request,'addblog.html')


def readmore(request,id):
    data = Blog.objects.get(id=id)
    comments = Comment_section.objects.all()
    context ={
        'data':data,
        'comments':comments,

    }
    return render(request,'readmore.html',context)

# def more(request):
#     data = Blog.objects.get()
#     return render(request,'readmore.html',{'data':data})


def search(request):
    searchinput = request.POST['search']
    if Blog.objects.filter(title__contains=searchinput).exists():
        data = Blog.objects.filter(title__contains=searchinput)
        return render (request,'home.html',{'data':data})
    else:
        messages.info(request,"No result found")
        return redirect ('home')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Try Matching Password")
            return redirect('signup')
    
    return render(request,'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Username / Password")
            return redirect('login')


    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')



def addcomment(request):
    if request.method == 'GET':
        form = commentform()
        return render(request,'addcoment.html',{'form':form})
    else:
        form = commentform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'addcoment.html')



# def shareblog(request):
    # if request.method == 'GET':
        # form = shareform()
        # return render(request,'shareblog.html',{'form':form})
    # else:
        # form = shareform(request.POST,request.FILES)
        # if form.is_valid():
            # form.save()
            # return redirect('/')
        # else:
            # return render(request,'shareblog.html')


def shareblog(request):
    if request.method=="POST":
        sender_mail = request.POST.get("sender_mail")
        sender_name = request.POST.get("sender_name")
        content = request.POST.get("content")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [sender_mail]
        subject = sender_name + "Here is your blog data"
        message = content
        ttt = Share_blg.objects.create(sender_mail=sender_mail,sender_name=sender_name,content=content)
        send_mail( subject,message,email_from, recipient_list)
        return redirect('/')
    return render(request,'shareblog.html')