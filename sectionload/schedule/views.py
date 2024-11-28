# sectionload/schedule/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'schedule/index.html')
