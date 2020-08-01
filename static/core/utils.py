from .models import Capitulo, Season
from django.core.paginator import Paginator


def consulta(id):
    try:
        return Capitulo.objects.get(id=id)
    except:
        return None


def generarTemporada(request, name_season):
    posts = Capitulo.objects.filter(
        state=True,
        published=False,
        season=Season.objects.get(name=name_season)
    )
    try:
        season = Season.objects.get(season=name_season)
    except:
        season = None

    contexto = {
        'posts': posts,
        'season': season,
    }
    return contexto


def generarCapitulos(request):
    posts = list(Capitulo.objects.filter(
        state=True,
        published=False
    ).order_by('number'))
    contexto = {
        'posts': posts}
    return contexto


def generarEspisodio(request):
    post = Capitulo.objects.filter(
        state=True,
        published=False
    ).values_list('id', flat=True)
    contexto = {'post': consulta(post)}
    return contexto
