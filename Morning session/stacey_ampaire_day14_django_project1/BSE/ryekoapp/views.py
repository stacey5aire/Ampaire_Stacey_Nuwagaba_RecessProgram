from django.shortcuts import render
from .models import SoilMoistureReading

# Create your views here.
def moisture_list_view(request):
    readings = SoilMoistureReading.objects.all().order_by('-timestamp')
    return render(request, 'ryekoapp/moisture_list.html', {'readings': readings})


