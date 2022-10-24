from django import forms

from .models import Olimp, Trier

class PostForm(forms.ModelForm):

    class Meta:
        model = Olimp
        fields = ('Title', 'Description','Site')
        
        
class Students(forms.ModelForm):

    class A:
        model = Trier
        fields = ('Name', 'Surname','Olympics')