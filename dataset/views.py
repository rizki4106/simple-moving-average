from django.shortcuts import render, redirect
from django.contrib import messages

# models
from .models import Data

# helper
from datetime import datetime
import pandas as pd

# middleware
from middleware.request import admin_middleware, method

@admin_middleware()
def index(request):
    """
    Menampilkan list produk
    """

    data = Data.objects.all().order_by('-nama')

    # definisikan data yang akan dikirim ke view
    context = {
        "title": "Data Produk",
        "page_name": "Data",
        "user": request.session.get("nama"),
        "data" : data,
    }

    return render(request, "data/index.html", context)

@admin_middleware()
def import_data(request):
    """
    Handle import data
    """

    # ambil file dari request
    files = request.FILES

    # membaca file excel yang diupload
    frame = pd.read_excel(files['file'])[["Tanggal", "Nama Barang", "Qty", "Nilai"]].iloc[:10]

    # menghilangkan string dari quantitas
    frame['Qty'] = frame['Qty'].apply(lambda x : int(x.split(' ')[0]))


    for row in frame.values:

        # cek apakah file sudah ada didalam database atau belum
        data_lama = Data.objects.filter(
            nama=row[1],
            tanggal=row[0].date()
        )

        if not data_lama.exists():

            # jika tidak ada maka masukan data baru
            data_baru = Data.objects.create(
                nama=row[1],
                tanggal=row[0].date(),
                qty=row[2],
                nilai=row[3]
            )

            data_baru.save()
    
    messages.add_message(request, messages.SUCCESS, "Berhasil menambahkan data")

    return redirect('/data')

@admin_middleware()
def delete_produk(request, id):
    """
    Menghapus data produk
    """

    # cek apakah produk ada atau tidak
    produk = Data.objects.filter(id=id)

    if produk.exists():

        # jika produk ada maka hapus
        produk.delete()

        messages.add_message(request, messages.SUCCESS, "Data berhasil dihapus")
    else:

        messages.add_message(request, messages.ERROR, "Data tidak ditemukan")
    
    return redirect('/data')
        