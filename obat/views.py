from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

# Obat
def create_obat(request):
    if request.POST:
        form = FormObat(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            form = FormObat()
            obat = {
                'form': form,
            }
            return render(request, 'obat/tambah_obat.html', obat)
    else:
        form = FormObat()
        obat = {
            'form': form
            }
        return render(request, 'obat/tambah_obat.html', obat)


def obat_list(request):
    obat = Obat.objects.all()
    return render(request, "obat/list_obat.html",{ "obats": obat,})


def update_obat(request, kode_obat):
    obats = Obat.objects.get(id=kode_obat)
    if request.method == 'POST':
        form = FormObat(request.POST, instance=obats)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('obat:update_obat', kode_obat=kode_obat)
    else:
        form = FormObat(instance=obats)
        obat = {
            'form': form,
            'obats': obats
            }
        return render(request, 'obat/edit_obat.html', obat)


def delete_obat(request, kode_obat):
    obats = Obat.objects.filter(id=kode_obat)
    obats.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'obat/list_obat.html')

# Fungsi Obat
def create_f_obat(request):
    if request.POST:
        form = FormFObat(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            form = FormFObat()
            f_obat = {
                'form': form,
            }
            return render(request, 'fungsi_obat/tambah_f_obat.html', f_obat)
    else:
        form = FormFObat()
        f_obat = {
            'form': form
            }
        return render(request, 'fungsi_obat/tambah_f_obat.html', f_obat)


def obat_f_list(request):
    f_obat = Fungsi_Obat.objects.all()
    return render(request, "fungsi_obat/list_f_obat.html",{ "f_obats": f_obat,})


def update_f_obat(request, kode_obat):
    obats = Obat.objects.get(id=kode_obat)
    if request.method == 'POST':
        form = FormObat(request.POST, instance=obats)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('obat:update_obat', kode_obat=kode_obat)
    else:
        form = FormObat(instance=obats)
        obat = {
            'form': form,
            'obats': obats
            }
        return render(request, 'obat/edit_obat.html', obat)


def delete_obat(request, kode_obat):
    obats = Obat.objects.filter(id=kode_obat)
    obats.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'obat/list_obat.html')
