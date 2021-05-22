from django import forms
# from dal import autocomplete

from .models import DataKlaim


class DataKlaimForm(forms.ModelForm):
    file_lain = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
            }
        ))

    class Meta:
        model = DataKlaim
        exclude = ('user',)
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'INPUT NAMA',
            }),
            'nik': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'INPUT NIK',
            }),
            'kpj': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'INPUT NO KPJ'
            }),

            'npp': forms.Select(attrs={
                'class': 'form-control'
            }),

            'tgl_lahir': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format="dd-mm-yyyy"),
            'tempat_lahir': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'INPUT TEMPAT LAHIR',
            }),
            'alamat': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'INPUT ALAMAT'
            }),
            'nama_ibu': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NAMA GADIS IBU KANDUNG'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'nama_pasangan': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NAMA SUAMI/ISTRI'
            }),
            'tgl_lahir_pasangan': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format="dd-mm-yyyy"),
            'nama_anak_s': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NAMA ANAK PERTAMA'
            }),
            'tgl_lahir_s': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format="dd-mm-yyyy"),
            'nama_anak_d': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NAMA ANAK KEDUA'
            }),
            'tgl_lahir_d': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }, format="dd-mm-yyyy"),
            'no_hp': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NO HANDPHONE/WA'
            }),
            'nama_rekening': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NAMA PEMILIK REKENING'
            }),
            'no_rekening': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NO REKENING'
            }),
            'file_kk': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'file_ktp': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'file_buku_nikah': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            # 'file_lain':forms.FileInput(attrs={
            #     'class':'form-control'
            # }),
        }
