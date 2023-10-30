from django.contrib import admin
from .models import Profile, Reactions

# Register your models here.
@admin.register(Profile)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'city')

@admin.register(Reactions)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('like_sender','like_receiver')