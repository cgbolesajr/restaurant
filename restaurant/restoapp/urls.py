from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = 'meals'


urlpatterns = [
    path('', views.meals_list, name='meal_list'),
    path('details/<slug:slug>', views.meal_detail, name='detail'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
