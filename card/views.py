from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    cards = Card.objects.all()

    form = CardForm()

    context = {'cards':cards, 'form':form}
    return render(request, 'index.html', context)