from django.contrib import admin

from .models import DataKlaim, Perusahaan, DaftarHRD, ApprovalHRD

admin.site.register(DataKlaim)
admin.site.register(Perusahaan)
admin.site.register(DaftarHRD)
admin.site.register(ApprovalHRD)
