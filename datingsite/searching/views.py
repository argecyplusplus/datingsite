from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Form
from .forms import RegisterForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# Create your views here.

class ProfileViewAll(View):
    '''вывод всех анкет'''
    def get(self, request):
        profiles = Form.objects.all()
        return render(request, 'searching/searching.html', {'profile_list': profiles})
 

class ProfileView(View):
    '''одна анкета'''
    def get(self, request, pk):
        profile = Form.objects.get(id=pk)
        return render(request, 'searching/form.html', {'profile': profile})

@login_required
def MyProfileView(request):
    return render (request, 'searching/myprofile.html')

@login_required
def ProfileViewAllRequest(request):
    return render (request, 'searching/searching.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("myprofile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    