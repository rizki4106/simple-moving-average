from django.db import models

class Data(models.Model):

    nama = models.CharField(max_length=50)
    kode = models.CharField(max_length=100, default="-")
    merk = models.CharField(max_length=10, default="-")
    satuan = models.CharField(max_length=10, default="-")

    def __str__(self):

        return f'{self.nama}'