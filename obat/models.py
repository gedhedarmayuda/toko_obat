from django.db import models

# Create your models here.


class Fungsi_Obat(models.Model):
    fungsi_obat = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.fungsi_obat)


class Obat(models.Model):
    kode_obat = models.CharField(max_length=10)
    nama_obat = models.CharField(max_length=20)
    supplier = models.CharField(max_length=20, null=True)
    stok = models.IntegerField()
    terjual = models.IntegerField()
    harga = models.CharField(max_length=30)
    jenis_obat_id = models.ForeignKey(Fungsi_Obat, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.kode_obat, self.nama_obat)