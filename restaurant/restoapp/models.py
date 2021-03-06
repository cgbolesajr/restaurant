from django.db import models
from django.utils.text import slugify

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    people = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal,self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
