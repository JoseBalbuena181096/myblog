import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)

# Apps entrada
from applications.entrada.models import (Entry)
# Apps home
from .models import (Home)
# form suscribe
from .forms import SuscribersForms, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
   
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        context['home'] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los articulos en home
        context['entradas_home'] = Entry.objects.entradas_en_home()
        # entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # enviamos formulario de suscripcion
        context['form'] = SuscribersForms
        return context
    
class SuscriberCreateView(CreateView):
    form_class = SuscribersForms
    success_url = '.'
    # para activar una vista necesitamos una url
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

