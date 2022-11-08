from django.shortcuts import render, redirect, get_object_or_404
from .models import Olimp, Trier, Olimp_Trier
import random
from .forms import PostForm, Students



def olimp_detail(request,pk):
    olimp = get_object_or_404(Olimp, pk=pk)
    return render(request, 'feed/olimp_detail.html', {'olimp': olimp})



def user_detail(request,pk):
    trier = get_object_or_404(Trier, pk=pk)
    olimp = list({trier.Olympics1,trier.Olympics2, trier.Olympics3,})
#    for i in range(len(olimp)):
#        olimp[i] = olimp[i][:-1]
    
    return render(request, 'feed/user_detail.html', {'trier': trier, 'olimp': olimp})


def user_lists(request):
    users = Trier.objects.all()
    
    s=[]
    for trier in users:
        
        s.append(trier)

    return render(request,'feed/user_lists.html' ,{'s': s})




def olimp_lists(request):
    olimps = Olimp.objects.all()
    s=[]
    for olimp in olimps:
        if 'inf' or 'mat' in olimp.tags:
            s.append(olimp)
            
    
    bic = {'table': [[ j*i for j in range(1,10)] for i in range(1,10) ] , 
           "name": "Hekto", "role": "Admin", 
           'bruh':[[ 'bruh ' for j in range(1,10)] for i in range(1,10) ],
           'randommass': [[ random.randint(0,11) for j in range(1,10)] for i in range(1,10)],
           'colors':['#FFC0CB',
                     '#4B0082',
                     '#FF0000',
                     '#FF4500',
                     '#F0E68C',
                     '#3CB371',
                     '#40E0D0',
                     '#87CEEB',
                     '#8B4513',
                     '#2F4F4F'][random.randint(0,9)],
                      's': s}
    
    return render(request,'feed/olimp_lists.html' ,bic)#{'s': s})


def olimp_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('olimp_lists')
    else:
        return render(request, 'feed/olimp_add.html', {'form': form})






def user_new(request):
    
    if request.method == "POST":
        form = Students(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('user_lists')
    else:
        form = Students()
    return render(request, 'feed/user_add.html', {'form': form})



