
from django.urls import include, path
from . import views

urlpatterns=[
    path('<int:category_id>/',views.post_by_category,name ='post_by_category')
]