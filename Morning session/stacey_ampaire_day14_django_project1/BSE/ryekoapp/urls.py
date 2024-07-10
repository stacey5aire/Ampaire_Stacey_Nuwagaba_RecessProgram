from django.urls import path
from .views import moisture_list_view

urlpatterns = [
    path('', moisture_list_view, name='moisture_list'),
]



