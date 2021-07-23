from django.shortcuts import render
from .models import Orgao


def OrgaosList(request):
    return render(request, "orgaos/orgaos.html", {
        'orgaos': Orgao.objects.all()
    })
