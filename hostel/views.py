from django.shortcuts import render
from .models import Hostel

# Create your views here.
def index(request):
    services_hostel = Hostel.objects.all()
    context = {'services_hostel': services_hostel}
    print(context)
    return render(request, "hostel/index.html", context)
    
def base(request):
    services_hostel = Hostel.objects.all()
    context = {'services_hostel': services_hostel}
    print(context)
    return render(request, "hostel/base.html", context)  