from django.shortcuts import render
from .models import Hostel

# Create your views here.
def index(request):
    return render(request, "hostel/index.html")