from django.forms import ModelForm
from django import forms
from obat.models import Obat


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
            'jenis_obat_id': forms.TextInput({'class': 'form-control'}),
        }
