# django library
from django.shortcuts import render, redirect
from django.contrib import messages

# python native
from datetime import datetime
from uuid import uuid4

# models
from .models import User

# middleware
from middleware.request import method

# helper
from helper.security import encrypt_password, verify_password

# Create your views here.
def index(request):
    """Menampilkan list user
    """

    # ambil data user
    user = User.objects.all().order_by("-created_at")

    # parameter halaman
    context = {
        "page_name": "Data Pengguna",
        "data": user,
        "user": request.session.get("nama")
    }

    # tampilkan halaman
    return render(request, "user/index.html", context)

@method('POST')
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
        password=encrypt_password(param.get("password")),
        created_at=datetime.now(),
        login_at=datetime.now()
    )

    # simpan data
    user.save()

    # tambahkan pesan
    messages.add_message(request, messages.SUCCESS, "Berhasil menambahkan data")

    # kembalikan ke halaman sebelumnya
    return redirect("/user")

@method('GET')
def delete_user(request, id):
    """
    View untuk menghapus user

    param:
        id : str -> id user
    """

    # ambil user
    user = User.objects.filter(user_id=id)

    # cek apakah user ada atau tidak
    if user.exists():

        # maka hapus user
        user.delete()

        # kirim pesan ke user
        messages.add_message(request, messages.SUCCESS, "Berhasil menghapus user")
    
    else:

        # jika tidak ada kirimkan pesan error
        messages.add_message(request, messages.ERROR, "User tidak ditemukan")
    
    return redirect('/user')

@method("GET")
def login(request):
    """
    Menampilkan halaman login
    """
    return render(request, "user/login.html")

@method('POST')
def do_login(request):
    """
    Melakukan autentikasi dengan mencocokan email serta password
    dari dalam database. Jika cocok akan diarahkan ke halaman home
    dan jika tidak cocok akan diarahkan ke halaman login

    param:
        email: str -> email user
        password: str -> password user

    method: POST
    """

    # ambil parameter
    param = request.POST

    # ambil user
    user = User.objects.filter(
        email=param.get("email")
    )

    # cek apakah email terdaftar
    if user.exists():

        # jika ada cek apakah password sesuai

        if verify_password(param.get("password"), user[0].password):

            # simpan sesi
            request.session["user_id"] = str(user[0].user_id)
            request.session['nama'] = user[0].nama
            request.session['email'] = user[0].email

            # jika password sama redirect ke home
            return redirect('/')
        else:

            messages.add_message(request, messages.ERROR, "Password salah")

            # jika tidak sama redirect ke halaman login
            return redirect("/user/login")
        
    else:

        # jika tidak ada kembalikan ke halaman login
        messages.add_message(request, messages.ERROR, "Email tidak terdaftar")

        return redirect("/user/login")

def logout(request):

    request.session['id'] = None
    request.session['nama'] = None

    return redirect('/user/login')