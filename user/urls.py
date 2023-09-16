from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list-user"),
    path('create', views.create_user, name="create-user"),
    path('delete/<str:id>', views.delete_user, name="delete-user"),
    path('login', views.login, name="login"),
    path('do-login', views.do_login),
    path('logout', views.logout)
]