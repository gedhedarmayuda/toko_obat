from django.urls import path, re_path
from . import views

app_name = 'obat'

urlpatterns = [
    path('create/', views.create_obat, name="create_obat"),
    path('', views.obat_list, name="obat_list"),
    re_path(r'^(?P<kode_obat>\d+)/update/$', views.update_obat, name="update_obat"),
    re_path(r'^(?P<kode_obat>\d+)/delete/$', views.delete_obat, name="delete_obat"),
]
