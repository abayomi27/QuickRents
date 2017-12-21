from django.shortcuts import render
from properties.models import Properties

# Create your views here.


def homepage(request):
    properties = Properties.objects.all()
    return render(request, 'properties/homepage.html', {'properties':properties})