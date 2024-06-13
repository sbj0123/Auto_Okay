from django.shortcuts import render
from core.core import get_auto_ok_instance, save_auto_ok_instance

# Create your views here.
def intro(request):
    return render(request, 'intro/intro.html')