
print("views.py is loaded")
from django.http import HttpResponse
from django.shortcuts import render
from about.models import About
from blogs.models import Category, Blog

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


