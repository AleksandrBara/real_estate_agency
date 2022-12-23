from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owners = models.ManyToManyField('property.Apparts_owner', verbose_name='Собственники')
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField(
        'Новостройка',
        default=None,
        null=True,
        blank=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(
        User,
        related_name="liked_flats",
        verbose_name='Кто лайкнул',
        blank=True
    )

    class Meta:
        verbose_name = 'Квартиры'
        verbose_name_plural = 'Квартиры'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор жалобы',
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира с жалобой',
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    text = models.TextField(verbose_name='Текст жалобы:')

    class Meta:
        verbose_name = 'Жалобы'
        verbose_name_plural = 'Жалобы'


class Apparts_owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=10)
    pure_phone = PhoneNumberField(
        verbose_name='Исправленный номер телефона',
        blank=True,
        null=True,
        default=None
    )
    flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности:',
        related_name='flats_owner',
        blank=True,
        default=None
    )

    def __str__(self):
        return self.name