from django.contrib import admin
from .models import Profile, Reactions, NewPair

# Register your models here.
@admin.register(Profile)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'city')

@admin.register(Reactions)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('like_sender','like_receiver')

@admin.register(NewPair)
class NewPairAdmin(admin.ModelAdmin):
    list_display = ('user1','user2')