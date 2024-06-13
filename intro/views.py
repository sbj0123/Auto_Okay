from django.shortcuts import render
from core.core import get_auto_ok_instance, save_auto_ok_instance

# Create your views here.
def intro(request):
    auto_ok = get_auto_ok_instance(request)
    save_auto_ok_instance(request, auto_ok)
    return render(request, 'intro/intro.html')