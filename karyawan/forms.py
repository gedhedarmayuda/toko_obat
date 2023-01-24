from django.forms import ModelForm
from django import forms
from karyawan.models import Karyawan


class FormKaryawan(ModelForm):
    class Meta:
        model = Karyawan
        fields = "__all__"

        widgets = {
            'no_karyawan': forms.TextInput({'class': 'form-control'}),
            'nama_lengkap': forms.TextInput({'class': 'form-control'}),
            'usia': forms.NumberInput({'class': 'form-control'}),
            'no_telp': forms.TextInput({'class': 'form-control'}),
            'email': forms.EmailInput({'class': 'form-control'}),
            'tempat_lahir': forms.TextInput({'class': 'form-control'}),
            'tanggal_lahir': forms.TextInput({'class': 'form-control'}),
            'jabatan_id': forms.Select({'class': 'form-control'}),
        }
