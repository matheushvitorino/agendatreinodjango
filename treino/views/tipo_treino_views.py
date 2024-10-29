from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.http import HttpResponse
from treino.forms import FormTipoTreino
from treino.models import TipoTreino
from django.urls import reverse_lazy


class TipoTreinoFormView(FormView):
    template_name='form.html'
    form_class= FormTipoTreino
    success_url=reverse_lazy('lista_tipo_treino')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class TipoTreinoListView(ListView):
    model = TipoTreino
    template_name = "tipotreino/lista_tipo_treino.html"
    context_object_name = "tipos"
    

class TipoTreinoDeleteView(DeleteView):
    model = TipoTreino
    template_name = "tipotreino/confirmacao_deletar_tipo_treino.html"
    success_url = reverse_lazy('lista_tipo_treino')
    context_object_name = "tipos"


    
class TipoTreinoUpdateView(UpdateView):
    model = TipoTreino
    template_name="form.html"
    form_class= FormTipoTreino
    success_url = reverse_lazy('lista_tipo_treino')
    
            