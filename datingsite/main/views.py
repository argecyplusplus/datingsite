from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request=request, template_name='main/main.html')