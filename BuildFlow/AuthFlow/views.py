from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class SplashView(View):
    def get(self, request):
        return render(request, 'authflow/splash.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'authflow/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(
                request, 'authflow/login.html',
                {'error':'Invalid credentials'}
                )
        

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'authflow/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'authflow/signup.html', {'form': form})
