from django.shortcuts import render
from .models import Olimp
# Create your views here.


def print_Matrix(A): 
    print()
    for row in A:
        for x in row:
            print('{:2d}'.format(x), end='')
        print()



def olimp_lists(request):
    olimps = Olimp.objects.all()
    s=[]
    for olimp in olimps:
        if 'inf' in olimp.tags:
            s.append(olimp)
            
    
    bic = {'table': [[ j*i for j in range(1,10)] for i in range(1,10) ] , "name": "Hekto", "role": "Admin"}
    
    return render(request,'feed/olimp_lists.html' ,bic)#{'s': s})

