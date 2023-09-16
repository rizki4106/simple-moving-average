from django.db import models

class Data(models.Model):

    nama = models.CharField(max_length=50)
    tanggal = models.DateField()
    qty = models.IntegerField()
    nilai = models.IntegerField()

    def __str__(self):

        return f'{self.nama}'