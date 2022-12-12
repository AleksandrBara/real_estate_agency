# Generated by Django 2.2.24 on 2022-12-12 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20221212_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flat',
            options={'ordering': ['created_at'], 'verbose_name': 'Квартиры', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Новостройка'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы:')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира с жалобой')),
            ],
        ),
    ]