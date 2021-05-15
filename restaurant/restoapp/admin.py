from django.contrib import admin
from .models import Meal, Category
# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Meal, MealAdmin)
admin.site.register(Category)
