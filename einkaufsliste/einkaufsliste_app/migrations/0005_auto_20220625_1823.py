# Generated by Django 3.2.5 on 2022-06-25 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('einkaufsliste_app', '0004_alter_customlist_list_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customlist',
            name='list_item',
        ),
        migrations.AddField(
            model_name='listitem',
            name='custom_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='einkaufsliste_app.customlist'),
            preserve_default=False,
        ),
    ]
