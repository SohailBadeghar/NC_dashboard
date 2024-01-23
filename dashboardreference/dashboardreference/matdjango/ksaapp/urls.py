from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('import/', views.import_from_excel, name='import_from_excel'),

]