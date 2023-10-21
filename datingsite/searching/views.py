from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Form
from random import shuffle

# Create your views here.

class FormViewAll(View):
    '''вывод всех анкет'''
    def get(self, request):
        forms = Form.objects.all()
        return render(request, 'searching/searching.html', {'form_list': forms})
 

class FormView(View):
    '''одна анкета'''
    def get(self, request, pk):
        form = Form.objects.get(id=pk)
        return render(request, 'searching/form.html', {'form': form})

@login_required
def MyProfileView(request):
    return render (request, 'searching/myprofile.html')