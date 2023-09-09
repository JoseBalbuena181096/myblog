from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import Entry, Category

# Create your views here.
 
class EntryListView(ListView):
    template_name = 'entrada/lista.html'
    context_object_name = 'entradas'
    paginate_by = 9


    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context
    
    # get queryset lo uso cuando queiro obtener un dato de la base de datos por metodo get
    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        # Consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado
    
# Detail view para mostrar el detalle de cada entrada
class EntryDetailView(DetailView):
    template_name = "entrada/detail.html"
    model = Entry