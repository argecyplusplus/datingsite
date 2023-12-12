from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request=request, template_name='main/main.html')
    
class ChangePasswordView(View):
    def post(self, request):
        return redirect('myprofile')