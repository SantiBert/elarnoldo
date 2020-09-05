from django.urls import path
from .views import Inicio, Buscador, Ingles, Latino, Capitulos, CapituloDetailView

urlpatterns = [

    path('post/<slug:slug>/', CapituloDetailView.as_view(),
         name='capitulo'),
    path('<str:lenguaje>/<str:season>/', Capitulos.as_view(), name="Capitulos"),


    path('ingles/', Ingles.as_view(),
         name='ingles'),
    path('latino/', Latino.as_view(),
         name='latino'),
    path('resultados/', Buscador.as_view(),
         name='buscar'),
    path('', Inicio.as_view(), name='index'),
]
