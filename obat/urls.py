from django.urls import path, re_path
from . import views

app_name = 'obat'

urlpatterns = [
    # Obat
    path('create/', views.create_obat, name="create_obat"),
    path('', views.obat_list, name="obat_list"),
    re_path(r'^(?P<kode_obat>\d+)/update/$', views.update_obat, name="update_obat"),
    re_path(r'^(?P<kode_obat>\d+)/delete/$', views.delete_obat, name="delete_obat"),
    
    # Fungsi Obat
    path('f_crete/', views.create_f_obat, name='create_f_obat'),
    path('f_obat_list/', views.obat_f_list, name='f_obat_list'),
    re_path(r'^(?P<nof_obat>\d+)/f_update/$', views.update_f_obat, name="update_f_obat"),
    re_path(r'^(?P<nof_obat>\d+)/f_delete/$', views.delete_f_obat, name="delete_f_obat"),
]
