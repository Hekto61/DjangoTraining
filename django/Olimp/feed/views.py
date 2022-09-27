from django.shortcuts import render
from .models import Olimp
# Create your views here.

def olimp_lists(request):
    olimps = Olimp.objects.all()
    return render(request,'feed/olimp_lists.html' ,{'olimps': olimps})

