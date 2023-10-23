from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Profile
from .forms import RegisterForm, MyProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# Create your views here.

class ProfileViewAll(View):
    '''вывод всех анкет'''
    def get(self, request):
        profiles = Profile.objects.all()
        return render(request, 'searching/searching.html', {'profile_list': profiles})
 
@login_required
def ProfileViewAllProtected(request):
    profiles = Profile.objects.all()
    return render (request, 'searching/searching.html', {'profile_list': profiles})

class ProfileView(View):
    '''одна анкета'''
    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        return render(request, 'searching/form.html', {'profile': profile})

@login_required
def MyProfileView(request):
    return render (request, 'searching/myprofile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = "/searching/myprofile"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class CreateMyProfile(View):
    #создание и редактирование анкеты
    def post(self, request):
        form = MyProfileForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            print (form)
        return redirect('/searching/')