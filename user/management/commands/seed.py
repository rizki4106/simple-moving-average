# django
from django.core.management.base import BaseCommand

# models
from user.models import User

# helper
from helper.security import encrypt_password
from datetime import datetime
from uuid import uuid4

class Command(BaseCommand):

    help = "Memasukan data default ke dalam database"

    def insert_admin(self):
        """
        Membuat admin baru
        """

        # cek apakah user sudah ada atau belum
        user_lama = User.objects.filter(
            email="admin@localhost"
        )

        if not user_lama.exists():

            # jika user tidak ada maka masukan
            user = User.objects.create(
                user_id=str(uuid4()),
                nama="Administrator",
                email="admin@localhost",
                password=encrypt_password("admin123"),
                created_at=datetime.now(),
                login_at=datetime.now()
            )

            user.save()

            print("Berhasil menambahkan admin")

    def handle(self, *args, **kwargs):

        self.insert_admin()