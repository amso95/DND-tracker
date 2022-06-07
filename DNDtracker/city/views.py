from django.shortcuts import render
from django.forms import ModelForm
from .models import City

def createCity(request):
    cityForm = CityForm(request.POST)
    if request.method == 'POST':
        if cityForm.is_valid():
            cityForm.save()
            cityForm = CityForm()
    return render(request, 'city/createCity.html', {'cityForm': cityForm })



class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'pdf']