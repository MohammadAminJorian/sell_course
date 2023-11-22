from django.urls import path
from .views import *
app_name='administrator'
urlpatterns = [
    path('login/' , home , name= 'home'),
    path('' , homee , name= 'homee'),
    
    path('course_View/' , course_View , name= 'course_View'),

    path('post/' , post , name= 'post'),
    path('course/' , course_View , name= 'course'),
    path('detail/<slug:slug>/', detail_Post, name="detail_Post"),
    path('video_Course/<int:id>/', video_Course, name="video_Course"),
    path('cart/<int:id>' , cart , name= 'cart'),
    path('myCourse/<int:id>/' , myCourse , name= 'myCourse'),
    ]
