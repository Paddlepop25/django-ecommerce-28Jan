from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
    
class RegisterForm(UserCreationForm):
    # you can change how it's shown by label. it will show the field in model by default; password1 ugly
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser # from models. to give reward points
        fields = ['email', 'username', 'password1', 'password2']
        
    # check if email user enter exist already in database when user register. if exist, error    
    def clean_email(self):
        # this is the email address the user has keyed in
        # clean email mean no special characters, won't cause issue when SQL injection, etc
        user_email = self.cleaned_data.get('email') 
        username = self.cleaned_data.get('username')
        
        User = get_user_model()
        # check if email is already in use
        # is comparable: SELECT * FOM User WHERE email='{}'.format(user_email)
        if User.objects.filter(email=user_email):
            raise forms.ValidationError('Email already in use. Email address must be unique')
            
        # django requirement to return whatever user key in.
        # returns this if no error
        return user_email    
        
    # clean_ function is for diff things like round up decimal points of whatever user has input. used to check for things    
        
