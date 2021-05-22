from .models import DaftarHRD
from django.contrib.auth.models import User

def userHRD(request):
    hrd = DaftarHRD.objects.get(user__username=request.user)
    if request.user == 'Anonymous':
        pass
    return {'hrd':hrd}