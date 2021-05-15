from django.shortcuts import render
from . import views
from .models import Meal, Category
# Create your views here.
def meals_list(request):
    meals = Meal.objects.all()
    categories = Category.objects.all()
    context = {'meals':meals, "categories": categories}
    return render(request, 'restoapp/meals_list.html', context)

def meal_detail(request,slug):
    meal_detail = Meal.objects.get(slug=slug)

    context = {'meal_detail': meal_detail}

    return render(request, 'restoapp/detail.html',context)
