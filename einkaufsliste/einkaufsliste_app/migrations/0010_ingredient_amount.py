# Generated by Django 3.2.5 on 2022-10-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('einkaufsliste_app', '0009_ingredient_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
