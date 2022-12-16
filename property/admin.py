from django.contrib import admin

from .models import Flat, Apparts_owner, Complaint

class FlatApparts_ownerline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['apparts_owner', 'flat']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display =  [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by', 'owners']
    inlines = [FlatApparts_ownerline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['author', 'flat', 'text']
    raw_id_fields = ['author', 'flat']


@admin.register(Apparts_owner)
class Apparts_ownerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'pure_phone',]
    raw_id_fields = ['flats']
    inlines = [FlatApparts_ownerline]



