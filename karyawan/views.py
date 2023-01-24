from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

# Karyawan


def create_karyawan(request):
    if request.POST:
        form = FormKaryawan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            form = FormKaryawan()
            karyawan = {
                'form': form,
            }
            return render(request, 'karyawan/tambah_karyawan.html', karyawan)
    else:
        form = FormKaryawan()
        karyawan = {
            'form': form
        }
        return render(request, 'karyawan/tambah_karyawan.html', karyawan)


def karyawan_list(request):
    karyawan = Karyawan.objects.all()
    return render(request, "karyawan/list_karyawan.html", {"karyawans": karyawan, })


def update_karyawan(request, no_karyawan):
    karyawans = Karyawan.objects.get(id=no_karyawan)
    if request.method == 'POST':
        form = FormKaryawan(request.POST, instance=karyawans)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('karyawan:update_karyawan', no_karyawan=no_karyawan)
    else:
        form = FormKaryawan(instance=karyawans)
        karyawan = {
            'form': form,
            'karyawans': karyawans
        }
        return render(request, 'karyawan/edit_karyawan.html', karyawan)


def delete_karyawan(request, no_karyawan):
    karyawans = Karyawan.objects.filter(id=no_karyawan)
    karyawans.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'karyawan/list_karyawan.html')

# Jabatan


def create_jabatan(request):
    if request.POST:
        form = FormJabatan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan")
            form = FormJabatan()
            jabatan = {
                'form': form,
            }
            return render(request, 'jabatan/tambah_jabatan.html', jabatan)
    else:
        form = FormJabatan()
        jabatan = {
            'form': form,
        }
        return render(request, 'jabatan/list_jabatan.html', {"jabatans": jabatan, })


def jabatan_list(request):
    jabatan = Jabatan.objects.all()
    return render(request, "jabatan/list_jabatan.html", {"jabatans": jabatan, })


def update_jabatan(request, no_jabatan):
    jabatans = Jabatan.objects.get(id=no_jabatan)
    if request.method == 'POST':
        form = FormJabatan(request.POST, instance=jabatans)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('karyawan:update_jabatan', no_jabatan=no_jabatan)
    else:
        form = FormJabatan(instance=jabatans)
        jabatan = {
            'form': form,
            'karyawans': jabatans
        }
        return render(request, 'jabatan/edit_jabatan.html', jabatan)


def delete_jabatan(request, no_jabatan):
    jabatans = Karyawan.objects.filter(id=no_jabatan)
    jabatans.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'jabatan/list_jabatan.html')
