


from django.shortcuts import render, get_object_or_404
from .models import Gul, Tur

def all_gullar(request):
    gullar = Gul.objects.all()
    return render(request, 'flowers/all_gullar.html', {'gullar': gullar})

def gullar_by_tur(request, tur_id):
    tur = get_object_or_404(Tur, pk=tur_id)
    gullar = tur.gullar.all()
    return render(request, 'flowers/gullar_by_tur.html', {'tur': tur, 'gullar': gullar})

def gul_detail(request, gul_id):
    gul = get_object_or_404(Gul, pk=gul_id)
    return render(request, 'flowers/gul_detail.html', {'gul': gul})



