# Generated by Django 2.2.24 on 2022-12-13 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20221212_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'Жалобы', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flat', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
