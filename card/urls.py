from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_card/<str:pk>', views.updateCard, name='update_card'),

    

]
