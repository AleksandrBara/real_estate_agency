# Generated by Django 2.2.24 on 2022-12-13 21:41

import phonenumbers
from django.db import migrations


def fix_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    country_code = 'RU'
    for flat in Flat.objects.iterator():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, country_code)
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = phonenumbers.format_number(
                parsed_number,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20221213_2100'),
    ]

    operations = [
        migrations.RunPython(fix_phone_number)
    ]
