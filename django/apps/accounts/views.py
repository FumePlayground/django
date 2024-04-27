
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    """Handle the login process for users."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Add an error message to the form if authentication fails
                form.add_error(None, 'Username or Password is incorrect')
        # Continue showing the form with errors if validation fails
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
