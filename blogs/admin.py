from django.contrib import admin
from .models import Category , Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured') # for display list of tabel in admin pannel
    search_fields = ('id','title','category__category_name','status','is_featured') #Here category is foreign key so declare name based on parent table
    
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)

