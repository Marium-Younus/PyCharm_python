from django.shortcuts import render,HttpResponse,redirect
from .models import u_contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from .models import Video
from .models import Book

def index(request):
    return  render(request,'index.html',{"session_user":request.session.get("username")})
def home(request):
    return  render(request,'home.html',{"session_user":request.session.get("username")})
def book(request):
    books = Book.objects.all()
    return render(request, 'book.html', context={'books': books,"session_user":request.session.get("username")})
def video(request):
  videos = Video.objects.all()
  return render(request, 'video.html', context={'videos': videos,"session_user":request.session.get("username")})
def registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

         my_user=User.objects.create_user(uname,email,pass1)
         my_user.save()
         return redirect('login')
    return  render(request,'registration.html',{"session_user":request.session.get("username")})
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            request.session['username'] = username
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return  render(request,'login.html',{"session_user":request.session.get("username")})
def contact(request):
    return  render(request,'contact.html',{"session_user":request.session.get("username")})
def funct_save(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['subject']
        d = request.POST['umsg']
        u_contact(c_name=a,c_email=b,c_subject=c,c_message=d).save()
        msg = 'Record Inserted Successfully'
        return  render(request,'contact.html',{'message':msg,"session_user":request.session.get("username")})
    else:
        return  HttpResponse('<h1>404 Page not found Error</h1>')
def funct_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('home')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            books = Book.objects.filter(book_title__contains=query)
            return render(request,'searchbar.html',{'books':books,"session_user":request.session.get("username")})
        else:
            print("no information to show")
            return request(request,'searchbar.html',{})