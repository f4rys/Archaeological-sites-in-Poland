from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('api/get_excavation_data/<str:inspire_id>/',
         views.get_excavation_data, name='get_excavation_data'),
]
