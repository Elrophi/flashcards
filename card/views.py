from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    cards = Card.objects.all()

    form = CardForm()

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'cards':cards, 'form':form}
    return render(request, 'index.html', context)

def updateCard(request, pk):
    card = Card.object.get(id=pk)

    form = CardForm(instance=card)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()

    context={'form':form}

    return(request, 'update_card.html', context)

def deleteCard(request, pk):
    item = Card.objects.get(id=pk)

    context={'item':item}
    return(request, 'delet_card.html')