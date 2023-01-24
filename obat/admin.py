from django.contrib import admin
from .models import *
# Register your models here.

class kolomObat(admin.ModelAdmin):
    list_display = ['kode_obat', 'nama_obat','supplier', 'stok','terjual', 'harga', 'jenis_obat_id', 'create_at']
    search_fields= ['kode_obat', 'nama_obat']
    list_filter = ('jenis_obat_id')
    list_per_page = 3

admin.site.register(Obat)
admin.site.register(Fungsi_Obat)