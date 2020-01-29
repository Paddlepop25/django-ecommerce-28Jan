from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import MyUser

# Create your views here.
def index(request):
    return render(request, 'Accounts/index.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('user_index'))

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] # extract out username from the form
        password = request.POST['password'] # extract out password from the form

        # I authenticate (that is, check if username and password matches)
        user = auth.authenticate(username=username, password=password)

        # Recreate form with the user's input submitted via POST
        login_form = LoginForm(request.POST)

        # only if a user is returned by auth.authenticate
        if user:
            # log a user in
            auth.login(user=user, request=request)
            messages.success(request, 'You have logged in successfully')
            return redirect(reverse('user_index'))
        else:
            # user is None
            login_form.add_error(None, "Invalid user name or password")
            return render(request, 'Accounts/login.template.html', {
            'login_form':login_form
        })
    else:
        # else if GET
        login_form = LoginForm()
        return render(request, 'Accounts/login.template.html', {
            'login_form':login_form
        }) 
        
@login_required        
def profile(request):
    # return render(request, 'Accounts/profile.template.html')
    User = MyUser
    user = User.objects.get(email=request.user.email)
    return render(request, 'Accounts/profile.template.html', {
        'user' : user
    })
    
def register(request):
    # when user submit form
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        # if all fields are vaild. django will check fields one by one
        # when check email, will check 'clean email' in forms
        if form.is_valid(): # if true because no error
            # if registration successful, save user, do form processing
            form.save() # this will create user
            
            # and log in user
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            # if user is authenticated
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'Registration successful!')
                return redirect(reverse('user_index'))
            else:
                messages.error(request, 'Sorry, unable to register your account')
                return redirect(reverse('index'))
        else:
            register_form = RegisterForm()
            return render(request, 'Accounts/register.template.html', {
                'form': register_form
            })
    else:    
        # if registration fail, just show form
        register_form = RegisterForm
        return render(request, 'Accounts/register.template.html', {
            'form': register_form
    })        