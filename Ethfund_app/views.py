from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Category, Projects
from django.contrib import messages
from django.http import HttpResponse

import json
# Create your views here.
def index(request):
    return render(request,"html/index-2.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not same')
            return redirect('register')
    else:
        return render(request,"html\\registration.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'html/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request,"html/about.html")

def projects(request):
    return render(request,"html/projects-1.html")

def news(request):
    return render(request,"html/news.html")

def contact(request):
    return render(request,"html/contact.html")

def singleProject(request):
    return render(request,"html/single-project.html")

def faq(request):
    return render(request,"html/faq.html")

# def projcreate(request):
#     return render(request,"html/create.html")

def create(request):
    # body = json.loads(request.body)
    if request.method == "POST":
        projectname = request.POST['projectname']
        projectdscp = request.POST['projectdscp']
        goal = request.POST['goal']
        deadline = request.POST['deadline']
        key = request.POST['key']
       
        image_uploaded = request.FILES['fileImg']
        video_uploaded = request.FILES['video']
        wallet_add = request.POST['contractAddress']
        # wallet_add = request.POST['walletAddress']
        # body = json.loads(request.body)
        # wallet_add  = body['wallet_add']
        # projectname = body['projectname']
        # projectdscp = body['projectdscp']
        # goal = body['goal']
        # deadline = body['deadline']
        # key = body['key']
        # image_uploaded = body['fileImg']
        # video_uploaded = body['video']
        # print(wallet_add)
        # wallet_add = request.POST.get('wallet_add')
        # print(wallet_add)
        project = Projects(projectname=projectname,projectdscp=projectdscp,goal=goal,deadline=deadline,key=key,image_uploaded=image_uploaded,video_uplaoded=video_uploaded,wallet_addr=wallet_add)
        project.save()
        # category_title = Category.objects.all()
        # context2['category'] = category_title
    return render(request,"html/create.html")
    # return HttpResponse(success)

def projects(request):
        context = {}
        projects = Projects.objects.all().filter(is_approved = True)
        context['projects'] = projects
        return render(request,"html/projects-1.html",context)

def details(request,id):
            # projects = Projects.objects.all().filter(id=id)
        # projects = Projects.objects.filter(id=id).first()
        projects = get_object_or_404(Projects,id=id)
        context={   
            'wallet_address' : projects.wallet_addr,
             'projects' : projects,
        }
        return render(request,"html/details.html",context)

def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exists!'})

# def ProjectAddress(request,adr):
#     if request.method=='POST':
        
def car(request):
    projects = Projects.objects.all()[:40:-1]
    context = {
        'projects':projects,
    }
    return render(request,"html\car.html",context)


def profile(request):
    return render(request,"html\profile.html")

def meta(request):
    projects = Projects.objects.last()
    context = {
        'projects':projects,
    }
    if request.method == "POST":
        wallet_id = request.POST.get('walletAddress')
        projects.wallet_addr = wallet_id
        projects.save()
        print(wallet_id)
    return render(request,"html\meta.html",context)