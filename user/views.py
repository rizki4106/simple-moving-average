# django library
from django.shortcuts import render, redirect
from django.contrib import messages

# python native
from datetime import datetime
from uuid import uuid4

# models
from .models import User

# Create your views here.
def index(request):
    """Menampilkan list user
    """

    # ambil data user
    user = User.objects.all().order_by("created_at")

    print(user)

    # parameter halaman
    context = {
        "page_name": "Forecasting",
        "data": user
    }

    # tampilkan halaman
    return render(request, "user/index.html", context)

def create_user(request):
    """
    Menambahkan user baru kedalam database jika email belum terdaftar
    method: POST
    params:
        nama : str -> nama user
        email: str -> email user
        password: str -> password

    returns:
        pesan: str -> session flash message ( pesan status query )
    """

    # ambil parameter
    param = request.POST

    # cek apakah email sudah terdaftar atau belum
    email = User.objects.filter(email=param.get("email"))

    if email.exists():

        # berikan pesan atau informasi
        messages.add_message(request, messages.ERROR, "Email sudah terdaftar")

        # jika email terdaftar maka arahkan ke halaman sebelumnya
        return redirect("/user")
    
    # jika email belum terdaftar maka masukan data
    user = User.objects.create(
        user_id=str(uuid4()),
        nama=param.get("nama"),
        email=param.get("email"),
        password=param.get("password"),
        created_at=datetime.now(),
        login_at=datetime.now()
    )

    # simpan data
    user.save()

    # tambahkan pesan
    messages.add_message(request, messages.SUCCESS, "Berhasil menambahkan data")

    # kembalikan ke halaman sebelumnya
    return redirect("/user")
    