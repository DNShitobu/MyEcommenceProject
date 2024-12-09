from django import forms
from .models import Customer
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone', 'address', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        
        # Send email confirmation
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(str(user.pk).encode())
        mail_subject = "Activate Your Account"
        message = f"Activate your account by clicking this link: /users/activate/{uid}/{token}/"
        send_mail(mail_subject, message, 'no-reply@yourdomain.com', [user.email])
        
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'phone', 'address', 'profile_picture']