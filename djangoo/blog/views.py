from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required 
from django.urls import reverse ,reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
import random
from kavenegar import *


def error_404_view(request, exception):
    return render(request, '404.html')


@login_required(login_url='/login/')
def Programs(request):
    return render(request , 'blog/shop/program.html')

@login_required(login_url='/login/')
def About(request):
    return render(request , 'blog/shop/about.html')



def Register(request):
    if request.user.is_authenticated:
        return redirect('administrator:homee')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
            user.save()
            return redirect('administrator:homee')
        else:
            messages.error(request, 'Something is wrong! Please try again', 'danger')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'administrator/Home/index.html',context)




class Well(SuccessMessageMixin):
    email_template_name = 'blog/welll/password_reset_email.html'
    subject_template_name = 'blog/welll/password_reset_subjects'





@login_required(login_url='/login/')
def ProfileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.Profile)
        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Update Successfully', 'success')
            return redirect('administrator:home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.Profile)
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'blog/profile/UpdateProfile.html', context)

def Logout_view(request):
    logout(request)
    return redirect('administrator:homee')

@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, 'your contact ', 'success')
        return redirect('administrator:home')

    profile = Profile.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile
    }
    return render(request, 'blog/contact/contact.html' , context)

@login_required(login_url='/login/')
def profile_view(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile , 'contact': profile
    }
    return render(request, 'blog/profile/Profile.html',context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'blog/passwordReset/password_reset.html'
    email_template_name = 'blog/passwordReset/password_reset_email.html'
    subject_template_name = 'blog/passwordReset/password_reset_subjects'
    success_message = ""

    success_url = reverse_lazy('blog:register')



@login_required(login_url='/login/')
def vip(request):
    if request.method == "POST":
        codevip = request.POST['vip']
        if codevip =="V2578946I31278054p":
            return redirect('blog:viip')
    
    return render(request, 'blog/Vip/vip.html')
    
    



@login_required(login_url='/login/')
def viip(request):
    return render(request, 'blog/Vip/isvip.html')


def login_phone(request):
    if request.method == 'POST':
        form = LoginPhoneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            global phone, random_code
            phone = f"{data['phone']}"
            random_code = random.randint(1000, 9999)
            sms = KavenegarAPI(
                "*")
            params = {
                'sender': '*',  # Array of String
                'receptor': phone,  # Array of String
                'message': f' {random_code} سلام این اولین تست است ',
            }
            response = sms.sms_send(params)
            return redirect('blog:verify_login_phone')
    else:
        form = LoginPhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/phone/login-phone.html', context)

@login_required(login_url='/login/')
def verify_login_phone(request):
    if request.method == 'POST':
        form = CodePhoneForm(request.POST)
        if form.is_valid():
            if str(random_code) == form.cleaned_data['verify_code']:
                profile = Profile.objects.filter(user_id=request.user.id).update(phone=phone)
                return redirect('blog:profile_view')
            else:
                messages.error(request, 'کد وارد شده اشتباه است')
    else:
        form = CodePhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/phone/verify-login-phone.html', context)



@login_required(login_url='/login/')
def contactss(request):
    contact = Contact.objects.filter(status='p').order_by('-publish')
    context = {
        'contact': contact
    }
    return render(request, 'blog/contact/allcontact.html', context)


@login_required(login_url='/login/')
def delete_user(request, email):
    if request.method == 'POST':
        try:
            user = MyUser.objects.get(email = email)
            user.delete()
        except Exception as e:
            print(e)
    else:
        messages.error(request, 'اکانت شما حذف شد')
    return render(request, 'blog/profile/delet.html')

#https://data-flair.training/blogs/django-send-email/
