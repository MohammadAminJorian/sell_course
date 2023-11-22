from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name='blog'
urlpatterns = [
    path('ProfileUpdate/' , ProfileUpdate , name="profileUpdate"),
    path('register/', Register, name="register"),
    path('delete_user/<str:email>/', delete_user, name="delete_user"),
    path('logout/' , Logout_view , name="logout"),
    path('contact/' , contact , name="contact"),
    path('all contacts/', contactss, name="contactss"),
    path('profileView/' , profile_view , name="profile_view"),
    path('programs/' ,Programs , name="programs"),
    path('about/' ,About , name="about"),
    path('vip/' ,vip , name="vip"),
    path('viiip/' ,viip , name="viip"),
    path('login_phone/' , login_phone , name="login_phone"),
    path('verify_login_phone/' , verify_login_phone , name="verify_login_phone"),

    path('password-reset/', ResetPasswordView.as_view(success_url=reverse_lazy('blog:password_reset_done')),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="blog/passwordReset/password_reset_done.html"),
         name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('blog:password_reset_complete'),
                                                     template_name='blog/passwordReset/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/passwordReset/password_reset_complete.html'),
         name='password_reset_complete'),


]