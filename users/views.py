from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:all-posts')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})




def login_view(request):
    """This view renders the login page of the users app."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:all-posts')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """This view logs the user out of the users app."""
    logout(request)
    return redirect('users:login')


def about(request):
    """This view renders the about page of the users app."""
    return render(request, 'users/about.html')


def contact(request):
    """This view renders the contact page of the users app."""
    return render(request, 'users/contact.html')
