from django.shortcuts import render, redirect
from .models import Obat
from .forms import FormObat
from django.contrib import messages
# Create your views here.


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
    obats = Obat.objects.filter(kode_obat=kode_obat)
    obats.delete()
    messages.success(request, "Data terhapus")
    return render(request, 'obat/tampil_obat.html')
