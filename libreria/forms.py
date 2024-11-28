# libreria/forms.py
from django import forms
from .models import Reseña

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['libro', 'contenido']
