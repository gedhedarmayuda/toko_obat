from django.urls import path, re_path
from . import views

app_name = 'karyawan'

urlpatterns = [
    # Karyawan
    path('create/', views.create_karyawan, name="karyawan_create"),
    path('', views.karyawan_list, name="karyawan_list"),
    re_path(r'^(?P<no_karyawan>\d+)/update/$', views.update_karyawan, name="update_karyawan"),
    re_path(r'^(?P<no_karyawan>\d+)/delete/$', views.delete_karyawan, name="delete_karyawan"),
    
    # Jabatan
    path('jabatan_create/', views.create_jabatan, name="jabatan_create"),
    path('jabatan_list/', views.jabatan_list, name='jabatan_list'),
    re_path(r'^(?P<no_jabatan>\d+)/jabatan_update/$', views.update_jabatan, name="update_jabatan"),
    re_path(r'^(?P<no_jabatan>\d+)/jabatan_delete/$', views.delete_jabatan, name="delete_jabatan"),
]
