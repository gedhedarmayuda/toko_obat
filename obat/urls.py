from django.urls import path, re_path
from . import views

app_name = 'obat'

urlpatterns = [
    path('create/', views.create_obat, name="create_obat"),
    path('', views.obat_list, name="obat_list"),
    re_path(r'^(?P<no_obat>\d+)/update/$', views.update_obat, name="obat_update"),
    re_path(r'^(?P<no_obat>\d+)/delete/$', views.delete_obat, name="obat_delete"),
]
