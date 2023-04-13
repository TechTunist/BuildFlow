from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages


# initial page when opeining app
class SplashView(View):
    def get(self, request):
        return render(request, 'authflow/splash.html')
    

# for existing users
class LoginView(View):
    def get(self, request):
        return render(request, 'authflow/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(
                request, 'authflow/login.html',
                {'error':'Invalid credentials'}
                )
        

# for new users
class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'authflow/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
                    
            return render(request, 'authflow/signup.html', {'form': form})
        

# logout user
# logout the user
def logout_user(request):
    logout(request)
    
    return redirect('authflow:splash')
        

# test view for dashboard redirect before dashboard app has been written
def dashboard(request):
    return HttpResponse("Pretend Dashboard")

