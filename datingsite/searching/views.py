from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Profile, Reactions
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
            return {'profileid':profile.id,'city':profile.city, 'gender': profile.gender}
    return {}

def load_defaults(request):
    profiles = Profile.objects.all()
    for profile in profiles:
        if str(profile.user) == str(request.user.username):
            return {'profileid':profile.id, 'name':profile.name, 'avatar':profile.avatar, 'city':profile.city, 'age': profile.age, 'gender': profile.gender, 'point_of_searching':profile.point_of_searching, 'social':profile.social, 'description':profile.description, 'minage':profile.age_search_min, 'maxage':profile.age_search_max}
    return {'name':'', 'avatar':'', 'city':'', 'age':'', 'gender':'', 'point_of_searching':'', 'social':'', 'description':'', 'minage':'', 'maxage':''}

        
class ProfileViewAllFiltered(View):
    #вывод всех анкет c фильтром
    def get(self, request):
        profiles = Profile.objects.all()
        profiles_filtered = []
        filterinfo = makefilters(request.user.username)
        if filterinfo == {}:
            return redirect ('myprofile')
        for profile in profiles:
            searching_gender = 'Девушка'
            searching_city = filterinfo['city']
            user_profile = Profile.objects.get(pk=filterinfo['profileid'])
            if filterinfo['gender'] == 'Девушка':
                searching_gender = 'Парень'
            if (profile.gender == searching_gender and 
                profile.city == searching_city and 
                user_profile.age_search_min<=profile.age<=user_profile.age_search_max):
                profiles_filtered.append (profile)
        return render (request, 'searching/searching.html', {'profile_list': profiles_filtered})


class ProfileView(View):
    '''одна анкета'''
    def get(self, request, pk, ):
        profile = Profile.objects.get(id=pk)
        return render(request, 'searching/profile.html', {'profile': profile})


@login_required
def startworking(request):
    return redirect('profiles')


@login_required
def MyProfileView(request):
    defaults = load_defaults(request)
    return render (request, 'searching/myprofile.html', {'username': request.user.id, 'dname':defaults['name'], 'davatar':defaults['avatar'], 'dcity':defaults['city'], 'dage': defaults['age'], 'dgender': defaults['gender'], 'dpoint_of_searching':defaults['point_of_searching'], 'dsocial':defaults['social'], 'ddescription':defaults['description'], 'dminage':defaults['minage'], 'dmaxage':defaults['maxage']})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    #success_url = "/searching/myprofile"
    success_url = '/'
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
                old_profile.age_search_min = form.cleaned_data.get('age_search_min')
                old_profile.age_search_max = form.cleaned_data.get('age_search_max')
                old_profile.save()
                print ('форма обновлена')
            else:
                form = form.save(commit=False)
                form.save()
            return redirect('profiles')
        else:
            return redirect(reverse_lazy ('myprofile'))
    

class ReactionsView(View):
    #вывод моих лайков
    def get(self, request):
        reactions = Reactions.objects.all()
        my_reactions = []
        for reaction in reactions:
            if reaction.like_receiver.username == request.user.username:
                my_reactions.append (reaction)
        return render(request, 'searching/reactions.html', {'profile_list': my_reactions})