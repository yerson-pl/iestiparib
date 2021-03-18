from django import forms
from .models import Postulante

class PostulanteForm(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'