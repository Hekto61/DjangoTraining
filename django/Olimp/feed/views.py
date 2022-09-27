from django.shortcuts import render
from .models import Olimp
# Create your views here.

def olimp_lists(request):
    olimps = Olimp.objects.all()
    s=[]
    for olimp in olimps:
        if 'inf' in olimp.tags:
            s.append(olimp)
    return render(request,'feed/olimp_lists.html' ,{'s': s})

