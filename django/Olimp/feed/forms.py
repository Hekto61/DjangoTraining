from django import forms

from .models import Olimp, Trier

class PostForm(forms.ModelForm):

    class Meta:
        model = Olimp
        fields = ('Title', 'Description','Site')
        
        
class Students(forms.ModelForm):

    class Meta:
        model = Trier
        fields = ('Name', 'LastName', 'Fomka','Olympics1','Olympics2','Olympics3',)