from django.forms import ModelForm
from django import forms
from obat.models import *

class FormObat(ModelForm):
    class Meta:
        model = Obat
        fields = "__all__"
        widgets = {
            'kode_obat': forms.TextInput({'class': 'form-control'}),
            'nama_obat': forms.TextInput({'class': 'form-control'}),
            'supplier': forms.TextInput({'class': 'form-control'}),
            'stok': forms.NumberInput({'class': 'form-control'}),
            'terjual': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.TextInput({'class': 'form-control'}),
            'jenis_obat_id': forms.Select({'class': 'form-control'}),
        }

class FormFungsi(ModelForm):
    class Meta:
        model = Fungsi_Obat
        fields = "__all__"
        widgets = {
            'fungsi_obat': forms.TextInput({'class': 'form-control'}),
            'keterangan': forms.TextInput({'class': 'form-control'}),
            }