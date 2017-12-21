from django.shortcuts import render, get_object_or_404
from properties.models import Properties

# Create your views here.


def homepage(request):
    properties = Properties.objects.all()
    return render(request, 'properties/homepage.html', {'properties': properties})


def apartment_detail(request, pk):
    apartment = get_object_or_404(Properties, pk=pk)
    return render(request, 'properties/apartment_details.html', {'property': apartment})