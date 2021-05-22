from django.urls import path, re_path

from . import views
# from .views import nppAutoComplete

urlpatterns = [
    path('', views.index, name='home-klaim'),
    path('daftar/', views.tambahKlaim, name='add'),
    path('hrd/klaim/', views.daftarKlaimHRD,
         name='hrd-klaim'),
    # path('hrd1/klaim/',views.daftarKlaimHRD1, name='hrd1-klaim'),
    path('hrd/klaim/all/', views.get_klaimhrds_json, name='all-klaim'),

    path('hrd/klaim/<int:id>/', views.get_klaimhrd_json, name='klaim-detail'),
    # path('klaim/zip/<int:id>/', views.zipAll, name='zip-file'),
    # re_path(
    #     r'^npp-autocomplete/$',
    #     nppAutoComplete.as_view(),
    #     name='npp-autocomplete',
    # ),

]
