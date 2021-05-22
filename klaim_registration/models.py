from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

NIK_VALIDATOR = RegexValidator("^\d{16}$",
    "Format NIK Tidak Sesuai")

HP_VALIDATOR = RegexValidator("^(08+[1-9])([0-9]{7,9})$", "Format NO HP TIDAK SESUA!!!")

NO_REK_VALIDATOR = RegexValidator("^\d{6,}$", "No Rekening Harus Berupa Angka")

EKSTENSI_VALIDATOR = RegexValidator(".*\.(jpg|JPG|gif|GIF|doc|DOC|pdf|PDF)", "Only Support PDF dan JPG")

SEGMEN = (
    ('PU', 'PENERIMA UPAH'),
    ('BPU', 'BUKAN PENERIMA UPAH'),
    ('JAKON', 'JASA KONSTRUKSI'),
)

STATUS = (
    ('1','BELUM MENIKAH'),
    ('2','MENIKAH')
)

STATUS_APPROVAL = (
    ('DALAM PEMERIKSAAN','DALAM PEMERIKSAAN'),
    ('DISETUJUI','DISETUJUI'),
    ('DITOLAK','DITOLAK')
)

class Perusahaan(models.Model):
    nama = models.CharField(max_length=200)
    npp = models.CharField(max_length=8)

    class Meta:
        ordering = ['-npp']
        verbose_name = "NPP"
        verbose_name_plural = "LIST NPP"

    def __str__(self):
        return self.nama
    
class DataKlaim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    nik = models.CharField(max_length=16, validators=[NIK_VALIDATOR])
    kpj = models.CharField(max_length=11)
    npp = models.ForeignKey(Perusahaan, on_delete=models.CASCADE)
    tgl_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=200)
    alamat = models.CharField(max_length=250)
    nama_ibu = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=1, default='1')
    nama_pasangan = models.CharField(max_length=100, null=True, blank=True)
    tgl_lahir_pasangan = models.DateField(blank=True, null=True)
    nama_anak_s = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir_s = models.DateField(null=True, blank=True)
    nama_anak_d = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir_d = models.DateField(null=True, blank=True)
    no_hp = models.CharField(max_length=15, validators=[HP_VALIDATOR])
    nama_rekening = models.CharField(max_length=100)
    no_rekening = models.CharField(max_length=16, validators=[NO_REK_VALIDATOR])
    file_kk = models.FileField(upload_to='kk/', validators=[EKSTENSI_VALIDATOR])
    file_ktp = models.FileField(upload_to='ktp/', validators=[EKSTENSI_VALIDATOR])
    file_buku_nikah = models.FileField(upload_to='buku-nikah/', validators=[EKSTENSI_VALIDATOR])
    file_lain = models.FileField(upload_to='lain/', null=True, blank=True, validators=[EKSTENSI_VALIDATOR])
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "DATA KLAIM"
        verbose_name_plural = "LIST DATA KLAIM"

    def __str__(self):
        return '{} - {}'.format(self.nik, self.nama)

class DaftarHRD(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    npp = models.ForeignKey(Perusahaan, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "LIST HRD"

    def __str__(self):
        return self.nama

class ApprovalHRD(models.Model):
    status = models.CharField(choices=STATUS_APPROVAL, default='DALAM PEMERIKSAAN', max_length=20)
    klaim = models.ForeignKey(DataKlaim, on_delete=models.CASCADE)
    hrd = models.ForeignKey(DaftarHRD, on_delete=models.CASCADE)
    keterangan = models.TextField(null=True, blank=True)
