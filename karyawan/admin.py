from django.contrib import admin
from .models import *
# Register your models here.

class kolomKaryawan(admin.ModelAdmin):
    list_display = ['no_karyawan', 'nama_lengkap','usia', 'no_telp','email', 'tempat_lahir', 'tanggal_lahir','jabatan_id','create_at']
    search_fields= ['no_karyawan', 'nama_lengkap']
    list_filter = ('jabatan_id')
    list_per_page = 3

admin.site.register(Karyawan)
admin.site.register(Jabatan)