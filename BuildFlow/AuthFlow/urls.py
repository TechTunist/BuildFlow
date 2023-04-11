from django.urls import path
from .views import SplashView, LoginView, SignupView


urlpatterns = [
    path('', SplashView.as_view(), name='splash'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
