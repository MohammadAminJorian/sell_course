from django.shortcuts import render, get_object_or_404 ,redirect
from .models import *
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from blog.models import MyUser , Profile
from .forms import *
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        return redirect('administrator:homee')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request , f'you are login now by :{request.user.email}')
            return redirect('administrator:homee')
        else:
            context = {
                "username": username,
                "errormessage": "User not found",

            }
            return render(request, "administrator/Home/index.html", context)
    else:
        return render(request, 'administrator/Home/index.html', {})






@login_required(login_url='/login/')
def homee(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile
    }
    return render(request , 'administrator/Home/index1.html' )


@login_required(login_url='/login/')
def post(request):
    post = Post.objects.filter(status='p').order_by('-publish')
    context = {'posts':post}
    return render(request , 'administrator/Home/post.html' , context)


@login_required(login_url='/login/')
def course_View(request):
    course = Course.objects.all().order_by('-publish')
    context = {
        'course': course
    }
    return render(request, 'administrator/Course/course-grid-2.html', context)


@login_required(login_url='/login/')
def detail_Post(request, slug):
    detail = get_object_or_404(Post, slug=slug , status='p')
    context = {
        'detail':detail
    }
    return render(request , 'administrator/Home/detail.html' , context)

@login_required(login_url='/login/')
def video_Course(request,id):
    video = Video.objects.filter(course_id=id)
    context = {
        'video':video
    }
    return render(request,'administrator/video/video.html',context)





@login_required(login_url='/login/')
def cart(request, id):
    user = request.user.id
    video = id
    if Cart.objects.filter(user_id=user, video_id=video).exists():
        return HttpResponse('از قبل خریداری شده است!')
    else:
        carts = Cart.objects.create(user_id=user, video_id=video)
        carts.save()
        return HttpResponse("ok")

@login_required(login_url='/login/')
def myCourse(request,id):
    cart = Cart.objects.filter(user_id=id)
    for carts in cart:
        video = Video.objects.filter(id = carts.video_id)
        context = {'video':video}
        return render(request, 'administrator/courseme/mycourse.html',context)

    return render(request, 'administrator/courseme/mycourse.html')



