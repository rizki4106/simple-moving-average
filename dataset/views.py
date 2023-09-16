from django.shortcuts import render

# middleware
from middleware.request import admin_middleware, method

@admin_middleware()
def index(request):
    """
    Menampilkan list produk
    """

    # definisikan data yang akan dikirim ke view
    context = {
        "title": "Data Produk",
        "page_name": "Data",
        "user": request.session.get("nama")
    }

    return render(request, "data/index.html", context)
