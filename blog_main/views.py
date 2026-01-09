
print("views.py is loaded")
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    print("home view is called")
    categories = Category.objects.all()
    print("categories",categories)
    featured_post = Blog.objects.filter(is_featured=True,status ='Published').order_by('updated_at')
    #return HttpResponse('<h2>Homepage</h2>')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts,
    }
    return render(request,'home.html',context)

