from django.db import models

class User(models.Model):

    user_id = models.UUIDField(primary_key=True, null=False)
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    login_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.nama} - last login at {self.login_at}"