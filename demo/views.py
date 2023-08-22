from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/admin')
def home(request):
    
    return render(request, 'demo/home.html')
