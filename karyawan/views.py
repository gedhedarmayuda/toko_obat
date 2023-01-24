from django.shortcuts import render, redirect
from .models import Karyawan
from .forms import FormKaryawan
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
    return render(request, "karyawan/list_karyawan.html",{ "karyawans": karyawan,})


def update_karyawan(request, id):
    karyawans = Karyawan.objects.get(no_karyawan=id)
    if request.method == 'POST':
        form = FormKaryawan(request.POST, instance=karyawans)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('ubah_karyawan', no_karyawan=id)
    else:
        form = FormKaryawan(instance=karyawans)
        karyawan = {
            'form': form,
            'karyawans': karyawans
            }
        return render(request, 'karyawan/ubah_karyawan.html', karyawan)


def delete_karyawan(request, no_karyawan):
    karyawans = Karyawan.objects.filter(no_karyawan=no_karyawan)
    karyawans.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'karyawan/tampil_karyawan.html')