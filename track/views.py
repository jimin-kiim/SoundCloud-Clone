from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from datetime import datetime
# Create your views here.


def a(request):
    return render(request, 'track/discover.html')
