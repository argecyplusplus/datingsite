from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Profile
from .forms import RegisterForm, MyProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import RedirectView
from django.contrib.auth.models import User

# Create your views here.

def makefilters(username):
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.username == username:
            return {'city':profile.city, 'age': profile.age, 'gender': profile.gender}


def load_defaults(request):
    profiles = Profile.objects.all()
    for profile in profiles:
        if str(profile.user) == str(request.user.username):
            return {'profileid':profile.id, 'name':profile.name, 'avatar':profile.avatar, 'city':profile.city, 'age': profile.age, 'gender': profile.gender, 'point_of_searching':profile.point_of_searching, 'social':profile.social, 'description':profile.description}
    return {'name':'', 'avatar':'', 'city':'', 'age':'', 'gender':'', 'point_of_searching':'', 'social':'', 'description':''}

class ProfileViewAll(View):
    #вывод всех анкет
    def get(self, request):
        profiles = Profile.objects.all()
        return render(request, 'searching/searching.html', {'profile_list': profiles})

        

class ProfileViewAllFiltered(View):
    #вывод всех анкет c фильтром
    def get(self, request):
        profiles = Profile.objects.all()
        profiles_filtered = []
        filterinfo = makefilters(request.user.username)
        for profile in profiles:
            searching_gender = 'Девушка'
            searching_city = filterinfo['city']
            if filterinfo['gender'] == 'Девушка':
                searching_gender = 'Парень'
            if (profile.gender == searching_gender and 
                profile.city == searching_city and 
                filterinfo['age']-4<=profile.age<=filterinfo['age']+4):
                profiles_filtered.append (profile)
        return render (request, 'searching/searching.html', {'profile_list': profiles_filtered, 'fgender':filterinfo['gender'], 'fage':filterinfo['age'], 'fcity':filterinfo['city']})


class ProfileView(View):
    '''одна анкета'''
    def get(self, request, pk, ):
        profile = Profile.objects.get(id=pk)
        return render(request, 'searching/profile.html', {'profile': profile})



@login_required
def MyProfileView(request):
    defaults = load_defaults(request)
    return render (request, 'searching/myprofile.html', {'username': request.user.id, 'dname':defaults['name'], 'davatar':defaults['avatar'], 'dcity':defaults['city'], 'dage': defaults['age'], 'dgender': defaults['gender'], 'dpoint_of_searching':defaults['point_of_searching'], 'dsocial':defaults['social'], 'ddescription':defaults['description']})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = "/searching/myprofile"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class CreateMyProfile(RedirectView):
    #создание и редактирование анкеты
    def post(self, request):
        #проверка есть ли анкеты
        already_created = False
        profiles = Profile.objects.all()
        for profile in profiles:
            if profile.user.username == request.user.username:
                already_created = True
                user_profile = profile.id
        

        form = MyProfileForm(request.POST)
        if form.is_valid():
            print ('форма валидная')
            
            if already_created:
                old_profile = Profile.objects.get(pk=user_profile)
                old_profile.name = form.cleaned_data.get('name')
                old_profile.avatar = form.cleaned_data.get('avatar')
                old_profile.age = form.cleaned_data.get('age')
                old_profile.gender = form.cleaned_data.get('gender')
                old_profile.point_of_searching = form.cleaned_data.get('point_of_searching')
                old_profile.city = form.cleaned_data.get('city')
                old_profile.description = form.cleaned_data.get('description')
                old_profile.social = form.cleaned_data.get('social')
                old_profile.save()
                print ('форма обновлена')
            else:
                form = form.save(commit=False)
                form.save()
                print ('форма сохранена')
            #тут подключение/обновление анкеты с аккаунтом
            print ("Анкета создана")
            return redirect('profiles')
        else:
            return redirect(reverse_lazy ('myprofile'))
    