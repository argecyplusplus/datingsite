from django.contrib import admin
from .models import Form

# Register your models here.
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name',)