from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from .models import Season, Capitulo
from .utils import generarTemporada, consulta, generarCapitulos, generarEspisodio
from django.db.models import Q
from next_prev import next_in_order, prev_in_order


class Inicio(View):
    def get(self, request, *args, **kwargs):
        contexto = generarCapitulos(request)
        return render(request, 'index.html', contexto)


class Ingles(ListView):
    queryset = Season.objects.filter(lenguje=True)
    context_object_name = "seasons"
    template_name = 'ingles.html'


class Latino(ListView):
    """
    Devuelve un template con la lista de Temporadas.
    """
    queryset = Season.objects.filter(lenguje=False)
    context_object_name = "seasons"
    template_name = 'latino.html'


class Capitulos(ListView):
    """
    Vista que devuelve todos los capitulos de una temporada
    """
    context_object_name = "capitulos"
    template_name = 'temporada.html'

    def get_queryset(self):
        capitulos = Capitulo.objects.filter(season__name=self.kwargs["season"])
        return capitulos


class CapituloDetailView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        print(slug)
        try:
            post = Capitulo.objects.get(slug=slug)
        except:
            post = None
        #contexto = generarEspisodio(request)

        contexto = {
            "post": post,

        }
        print(post)
        return render(request, 'capitulo.html', contexto)


class Buscador(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        if queryset:
            posts = Post.objects.filter(
                Q(name__icontains=queryset) |
                Q(descripcion__icontains=queryset),
                state=True,
                published=True
            ).distinct()

        return render(request, 'resultado.html', {'posts': posts})
