from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from hotel_data.models import Hotel, City

# Create your views here.
def index(request):
    city_list = City.objects.all()
    context = {
        'city_list': city_list,
    }
    return render(request, 'index.html', context)

def hotels(request):
    # Grab query parameter
    city_id = request.GET.get('city_id') 
    hotel_list = Hotel.objects.filter(city_id = city_id)
    context = {
        'hotel_list': hotel_list,
    }
    return render(request, 'index.html', context)