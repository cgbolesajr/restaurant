from django.urls import path
from . import views


app_name = 'aboutus_list'

urlpatterns = [
        path('', views.aboutus_list, name='aboutus_list')
]
