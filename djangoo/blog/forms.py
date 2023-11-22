from django import forms
from .models import *


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_Confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'username']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password_Confirmation'] and data['password'] and data['password_Confirmation'] != data['password']:
            raise forms.ValidationError('Passwords are not the same')
        return data['password_Confirmation']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password_Confirmation'])
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'username']


class LoginPhoneForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']


class CodePhoneForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['verify_code']





class vipUserCreateForm(forms.ModelForm):
    codevip = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['codevip']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user