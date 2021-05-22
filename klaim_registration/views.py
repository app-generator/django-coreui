from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Subquery, OuterRef, IntegerField
from django.http import JsonResponse
# from dal import autocomplete

from .form import DataKlaimForm
from .models import DataKlaim, Perusahaan, ApprovalHRD, DaftarHRD


@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user

    is_admin = User.objects.filter(username=user, is_superuser=True)

    # is_hrd = DaftarHRD.objects.get(user=user)
    if is_admin:
        datas = DataKlaim.objects.all()
        size = datas.count()
    else:
        datas = DataKlaim.objects.filter(user=user).annotate(status_approve=Subquery(
            ApprovalHRD.objects.filter(klaim_id=OuterRef('pk')).values('status')[:1]))
        size = datas.count()
    context = {
        'datas': datas,
        'size': size,
    }

    return render(request, 'klaim_registration/index.html', context)


@login_required(login_url='/accounts/login/')
def tambahKlaim(request):
    user = request.user
    cekKlaim = ApprovalHRD.objects.filter(
        klaim__user__username=user, status='DISETUJUI')
    if cekKlaim.exists():
        messages.warning(request, "Akun anda sudah pernah mengajukan KLAIM")
        return redirect(reverse('home-klaim'))
    # print(user.is_authenticated)
    if request.method == 'POST':
        forms = DataKlaimForm(request.POST, request.FILES)
        if forms.is_valid():
            post = forms.save(commit=False)
            # post.user = user
            post.user = user

            # post.npp = request.POST['npp']
            post.save()
            hrd = DaftarHRD.objects.get(npp_id=post.npp_id)
            ApprovalHRD.objects.create(klaim_id=post.id, hrd_id=hrd.id)

            return redirect('home')

    else:
        forms = DataKlaimForm()
    return render(request, 'klaim_registration/daftar.html', {'forms': forms})


@login_required(login_url='/accounts/login/')
def daftarKlaimHRD(request):
    # print(request.user)
    datas = ApprovalHRD.objects.all().filter(
        hrd__user__username=request.user, status='DALAM PEMERIKSAAN')
    if not datas.exists():
        datas = ApprovalHRD.objects.all().filter(hrd__user__username=request.user)
        # detail = datas.select_related('klaim')
        # print(detail)
    if request.is_ajax:
        # print(request.POST.get('status'))
        ApprovalHRD.objects.filter(id=request.POST.get('id')).update(
            status=request.POST.get('status'), keterangan=request.POST.get('keterangan'))
        # return JsonResponse({'data': 'sucess'})
    context = {
        'datas': datas,
        # 'detail':detail,
    }

    return render(request, 'klaim_registration/hrd.html', context)


@login_required(login_url='/accounts/login/')
def daftarKlaimHRD1(request):
    # print(request.user)
    datas = ApprovalHRD.objects.all().filter(
        hrd__user__username=request.user, status='DALAM PEMERIKSAAN')
    if not datas.exists():
        datas = ApprovalHRD.objects.all().filter(hrd__user__username=request.user)
        detail = datas.select_related('klaim')
        # print(detail)
    if request.is_ajax:
        # print(request.POST.get('status'))
        ApprovalHRD.objects.filter(id=request.POST.get('id')).update(
            status=request.POST.get('status'), keterangan=request.POST.get('keterangan'))
        # return JsonResponse({'data': 'sucess'})
    context = {
        'datas': datas,
        'detail': detail,
    }

    return render(request, 'klaim_registration/hrd1.html', context)


@login_required(login_url='/accounts/login/')
def get_detail_tk(request, id=None):
    instance = get_object_or_404(DataKlaim, id=id)
    context = {
        'instance': instance
    }
    return render(request, 'klaim_registration/modal.html', context)


def get_klaimhrd_json(request, id):
    hrd_qs = list(ApprovalHRD.objects.all().filter(hrd__user__username=request.user, id=id).values(
        'id', 'klaim__nama', 'klaim__nik', 'klaim__kpj', 'klaim__npp', 'klaim__tempat_lahir', 'klaim__tgl_lahir',
        'klaim__nama_ibu', 'klaim__status', 'klaim__nama_rekening', 'klaim__no_rekening', 'klaim__no_hp'
    ))

    return JsonResponse({'data': hrd_qs})


def get_klaimhrds_json(request):
    hrd_qs = list(ApprovalHRD.objects.all().filter(hrd__user__username=request.user).values(
        'klaim_id', 'klaim__nama', 'klaim__nik', 'klaim__kpj', 'klaim__npp', 'klaim__tempat_lahir', 'klaim__tgl_lahir',
        'klaim__nama_ibu', 'klaim__status', 'klaim__nama_rekening', 'klaim__no_rekening', 'klaim__no_hp'
    ))

    return JsonResponse({'data': hrd_qs})


@login_required(login_url='/accounts/login/')
def daftarSeluruhKlaim(request):
    is_hrd = ApprovalHRD.objects.all().filter(
        hrd__user__username=request.user)[0]
    print(is_hrd)
    if is_hrd:
        datas = is_hrd.all()
        return render(request, 'klaim_registration/hrd.html', {'datas': datas})
    else:
        return redirect('home-klaim')


# def zipAll(request, id):
#     import zipfile
#     from io import StringIO
#     import os

#     datas = DataKlaim.objects.get(user__username=user.request, pk=id)
#     for data in datas:
#         nama = data.nama
#         file_kk = data.file_kk.file
#         file_ktp = data.file_ktp.file
#         file_buku_nikah = data.file_buku_nikah.file
#         file_lain = data.file_lain.file
#     filenames = [file_buku_nikah, file_kk, file_ktp, file_lain]
#     subdir = nama
#     zip_filename = "%s.zip" % subdir
#     s = StringIO()
#     zf = zipfile.ZipFile(s, "w")
#     for fpath in filenames:
#         fdir, fname = os.path.split(fpath)
#         zip_path = os.path.join(subdir, fname)
#         zf.write(fpath, zip_path)
#     zf.close()
#     resp = HttpResponse(s.getvalue(), mimetype="application/x-zip-compressed")
#     # ..and correct content-disposition
#     resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

#     return resp
