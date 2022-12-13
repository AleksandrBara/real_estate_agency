from django.contrib import admin

from .models import *


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
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
    raw_id_fields = ['liked_by']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['author', 'flat', 'text']
    raw_id_fields = ['author', 'flat']

class Apparts_ownerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'pure_phone',]
    raw_id_fields = ('flats')

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Apparts_owner, Apparts_ownerAdmin)

