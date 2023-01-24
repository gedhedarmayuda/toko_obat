from django.urls import path, re_path
from . import views

app_name = 'karyawan'

urlpatterns = [
    path('create/', views.create_karyawan, name="karyawan_create"),
    path('', views.karyawan_list, name="karyawan_list"),
    re_path(r'^(?P<no_karyawan>\d+)/update/$', views.update_karyawan, name="update_karyawan"),
    re_path(r'^(?P<no_karyawan>\d+)/delete/$', views.delete_karyawan, name="karyawan_delete"),
]
