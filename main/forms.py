from django import forms 
from .models import Player

class PlayerEntry(forms.ModelForm):
    class Meta:
        model = Player 
        fields = ['first_name', 'last_name', 'country', 'franchise', 'runs', 'wickets']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'runs' : forms.TextInput(attrs={'class' : 'form-control'}),
            'wickets' : forms.TextInput(attrs={'class' : 'form-control'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control'}),
            'franchise' : forms.TextInput(attrs={'class' : 'form-control'})
        }