
print("views.py is loaded")
from django.http import HttpResponse
from django.shortcuts import redirect, render
from about.models import About
from blog_main.forms import RegistrationForm
from blogs.models import Category, Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def home(request):
    print("home view is called")
    categories = Category.objects.all()   # we have declared category as nav bar using context
    print("categories",categories)
    featured_post = Blog.objects.filter(is_featured=True,status ='Published').order_by('updated_at')
    #return HttpResponse('<h2>Homepage</h2>')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    
    #About us 
    try:
        about = About.objects.get()
    except:
        about = None

    
    context = {
        'categories':categories,   # we have declared category as nav bar using context
        'featured_post':featured_post,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)


# register page function
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.erros)
    else:
        form = RegistrationForm()
        context = {'form':form}
        return render(request,'register.html',context)
    
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # this cleaned form data is form web page input type field name
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form = AuthenticationForm()
    context = {'form':form,}
    return render(request,"login.html",context)

def logout(request):
    auth.logout(request)
    return redirect('home')