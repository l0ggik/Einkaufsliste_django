# Generated by Django 3.2.5 on 2022-06-25 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('einkaufsliste_app', '0002_purchasingitem_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='CustomList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('list_item', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='einkaufsliste_app.listitem')),
            ],
        ),
    ]
