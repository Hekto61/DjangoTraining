from django import forms

from .models import Olimp

class PostForm(forms.ModelForm):

    class Meta:
        model = Olimp
        fields = ('Title', 'Description','Site')