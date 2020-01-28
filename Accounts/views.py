from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm
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