from django  import forms
from django.forms import ModelForm
from .models import *


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'