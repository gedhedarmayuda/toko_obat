from django.db import models

# Create your models here.


class Jabatan(models.Model):
    jabatan = models.CharField(max_length=20)

    def __str__(self):
        return self.jabatan


class Karyawan(models.Model):
    no_karyawan = models.CharField(max_length=10)
    nama_lengkap = models.TextField()
    usia = models.IntegerField()
    no_telp = models.CharField(max_length=20)
    email = models.EmailField()
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.CharField(max_length=20)
    jabatan_id = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.no_karyawan, self.nama_lengkap)