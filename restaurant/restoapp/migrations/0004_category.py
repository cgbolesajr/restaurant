# Generated by Django 3.2 on 2021-04-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0003_meal_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]