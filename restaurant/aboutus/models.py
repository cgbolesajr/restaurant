from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to='aboutus/')

    class Meta:
        verbose_name_plural = 'AboutUs'

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'WhyChooseUs'

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    def __str__(self):
        return self.name
