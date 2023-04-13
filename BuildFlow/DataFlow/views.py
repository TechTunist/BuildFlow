from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, authenticate
from django.shortcuts import render
from .models import Project, Data, Address



@login_required(login_url='/authenticate')
def home(request):

    if request.user.is_authenticated:
        print("Auth approved")

    user = request.user

    project = Project.objects.get(client=user)
    # address = Address.objects.filter(project=project)
    # data = Data.objects.filter(address=address)

    print(project)

    context = {
        # 'data': data,
        # 'address': address,
        'project': project
        }

    return render(request, 'dataflow/home.html', context)


# logout the user
def logout_user(request):
    logout(request)
    
    return redirect('authflow/auth')


