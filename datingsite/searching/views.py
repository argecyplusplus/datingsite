import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Profile, Reactions, NewPair
from .forms import RegisterForm, MyProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import RedirectView
from django.contrib.auth.models import User

# Create your views here.

def makefilters(request):
    try:
        profile = Profile.objects.get(user = User.objects.get(username = request.user.username))
        return {'profileid':profile.id,'city':profile.city, 'gender': profile.gender}
    except Exception:
        return {}

def load_defaults(request):
    try:
        profile = Profile.objects.get(user = User.objects.get(username = request.user.username))
        return {'profileid':profile.id, 'name':profile.name, 'avatar':profile.avatar, 'city':profile.city, 'age': profile.age, 'gender': profile.gender, 'point_of_searching':profile.point_of_searching, 'social':profile.social, 'description':profile.description, 'minage':profile.age_search_min, 'maxage':profile.age_search_max}
    except Exception:
        return {'name':'', 'avatar':'photos/default_avatar.jpg', 'city':'', 'age':'', 'gender':'', 'point_of_searching':'', 'social':'', 'description':'', 'minage':'', 'maxage':''}

def cleardata():
    usedphotos = []
    for profile in Profile.objects.all():
        usedphotos.append (str(profile.avatar)[13:])
    for files in os.walk("media/photos/users"):  
        for file in files[2]:
            if not(file in usedphotos):
                os.remove('media/photos/users/' + str(file))

def countUnchecked(request):
    count = 0
    reactions = Reactions.objects.all()
    pairs = NewPair.objects.all()
    for reaction in reactions:
        if reaction.like_receiver == request.user and not(reaction.viewed):
            #maybe delete "and not(reaction.viewed)"
            count +=1
    for pair in pairs:
        if pair.user1 == request.user and not (pair.viewed1):
            count +=1
        if pair.user2 == request.user and not (pair.viewed2):
            count +=1
    return count

class ProfileViewAllFiltered(View):
    #вывод всех анкет c фильтром
    def get(self, request):
        profiles = Profile.objects.all()
        reactions = Reactions.objects.all()
        pairs = NewPair.objects.all()
        
        #удаление рассмотренных профилей
        profiles_i_liked = []
        for reaction in reactions:
            if reaction.like_sender == request.user:
                profiles_i_liked.append (reaction.like_receiver_profile)
        profiles_we_paired = []
        for pair in pairs:
            if pair.user1 == request.user:
                profiles_we_paired.append (pair.profile2)
            elif pair.user2 == request.user:
                profiles_we_paired.append (pair.profile1)
       
        #счетчик непрочитанных
        unchecked_counter = countUnchecked(request)
        
        #отфильтрованный вывод
        filterinfo = makefilters(request)
        if filterinfo == {}:
            #если анкета не заполнена
            return redirect ('myprofile')
        profiles_filtered = []
        for profile in profiles:
            searching_gender = 'Девушка'
            searching_city = filterinfo['city']
            user_profile = Profile.objects.get(pk=filterinfo['profileid'])
            if filterinfo['gender'] == 'Девушка':
                searching_gender = 'Парень'
            if (profile.gender == searching_gender and 
                profile.city == searching_city and 
                user_profile.age_search_min<=profile.age<=user_profile.age_search_max and
                not(profile in profiles_i_liked) and not (profile in profiles_we_paired)):
                profiles_filtered.append (profile)
        
        return render (request, 'searching/searching.html', {'profile_list': profiles_filtered, 'unchecked_counter': unchecked_counter})



class ProfileView(View):
    #вывод анкеты человека который отправил лайк и полученных пар
    def get(self, request, pk):

        profile = Profile.objects.get(id=pk)
        showsocial = 0
        #просмотр новой пары
        try:
            newpair = NewPair.objects.get (user1 = request.user, profile2 = profile)
            newpair.viewed1 = True
            newpair.save()
            showsocial = 1
        except Exception:
            pass
        try:
            newpair = NewPair.objects.get (user2 = request.user, profile1 = profile)
            newpair.viewed2 = True
            newpair.save()
            showsocial = 1
        except Exception:
            pass
        #просмотр входящей анкеты
        try:
            reaction = Reactions.objects.get (like_receiver = request.user, like_sender_profile = profile)
            print (f'анкета {reaction} найдена и  просмотрена')
            reaction.viewed = True
            reaction.save()
            reply = 1
        except Exception:
            reply = 0

        return render(request, 'searching/profile.html', {'profile': profile, 'reply': reply, 'showsocial':showsocial})
    


@login_required
def startworking(request):
    return redirect('profiles')


@login_required
def MyProfileView(request):
    cleardata() #чистка лишних файлов в media
    defaults = load_defaults(request)
    return render (request, 'searching/myprofile.html', {'username': request.user.id, 'dname':defaults['name'], 'davatar':defaults['avatar'], 'dcity':defaults['city'], 'dage': defaults['age'], 'dgender': defaults['gender'], 'dpoint_of_searching':defaults['point_of_searching'], 'dsocial':defaults['social'], 'ddescription':defaults['description'], 'dminage':defaults['minage'], 'dmaxage':defaults['maxage']})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class CreateMyProfile(RedirectView):
    #создание и редактирование анкеты
    def post(self, request):
        #проверка есть ли анкеты
        try:
            #форма найдена
            old_profile = Profile.objects.get(user = User.objects.get(username = request.user.username))
            form = MyProfileForm(request.POST, request.FILES)
            if form.is_valid():
                old_profile.name = form.cleaned_data.get('name')
                if (form.cleaned_data.get('avatar') != 'photos/default_avatar.jpg'):
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
                return redirect('profiles')
            return redirect(reverse_lazy ('myprofile'))
        except Exception:
            #форма не найдена
            form = MyProfileForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = User.objects.get(username=request.user.username)
                form.save()
                return redirect('profiles')
            return redirect(reverse_lazy ('myprofile'))
   

class ReactionsView(View):
    #вывод моих лайков и полученных пар
    def get(self, request):
        #полученные лайки
        reactions = Reactions.objects.all()
        my_reactions = []
        marked_profiles = [] #collect ids
        for reaction in reactions:
            if reaction.like_receiver.username == request.user.username:
                # - если непросмотрена то с отметкой
                if reaction.viewed == False:
                    marked_profiles.append(reaction.like_sender_profile.id)
                my_reactions.append (reaction.like_sender_profile)
        #полученные пары
        pairs = NewPair.objects.all()
        my_pairs = []
        for pair in pairs:
            if pair.user1.username == request.user.username:
                # - если непросмотрена то с отметкой
                if pair.viewed1 == False:
                    marked_profiles.append(pair.profile2.id)
                my_pairs.append(pair.profile2)
            if pair.user2.username == request.user.username:
                # - если непросмотрена то с отметкой
                if pair.viewed2 == False:
                    marked_profiles.append(pair.profile1.id)
                my_pairs.append(pair.profile1)
        return render(request, 'searching/reactions.html', {'profile_list': my_reactions, 'pair_list':my_pairs, 'marked_profiles': marked_profiles})
    

class ReactView(View):
    def get(self, request, pk):
        liked_profile = Profile.objects.get(id=pk) # анкета которую лайкнули
        sender = User.objects.get(username=request.user.username)
        new_reaction = Reactions.objects.get_or_create (like_sender = sender, like_receiver = liked_profile.user, like_sender_profile = Profile.objects.get(user = sender), like_receiver_profile = liked_profile)
        return redirect ('profiles')

class ReactReplyView(View):
        #полученная анкета понравилась
        def get(self, request, pk):
            try:
                #создание модели NewPair
                sender_profile = Profile.objects.get(id=pk) #анкета отправителя
                new_reaction = Reactions.objects.get (like_receiver = request.user, like_sender_profile = sender_profile)
                new_pair = NewPair.objects.get_or_create(user1 = new_reaction.like_sender, user2 = new_reaction.like_receiver, profile1 = new_reaction.like_sender_profile, profile2=  new_reaction.like_receiver_profile, viewed2 = True)
                #вывод информации
                showedprofile = NewPair.objects.get(user1 = new_reaction.like_sender, user2 = new_reaction.like_receiver, profile1 = new_reaction.like_sender_profile, profile2=  new_reaction.like_receiver_profile, viewed2 = True).profile1
                new_reaction = new_reaction.delete()
                return render (request, 'searching/newpair.html', {'profile': showedprofile})
            except Exception:
                return redirect ('reactions')

class ReactReplyViewDislike(View):
    #полученная анкета не понравилась
    def get(self, request, pk):
        sender_profile = Profile.objects.get(id=pk) #анкета отправителя
        new_reaction = Reactions.objects.get (like_receiver = request.user, like_sender_profile = sender_profile).delete()
        return redirect ('profiles')