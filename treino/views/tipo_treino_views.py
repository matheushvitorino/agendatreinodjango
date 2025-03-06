from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from treino.forms import FormTipoTreino
from treino.models import TipoTreino
from django.urls import reverse_lazy

class TipoTreinoFormView(LoginRequiredMixin,FormView):
    template_name='form.html'
    form_class= FormTipoTreino
    success_url=reverse_lazy('lista_tipo_treino')
    
    def form_valid(self,form):
        ttreino_salvo =form.save(commit=False)
        ttreino_salvo.usuario = self.request.user
        ttreino_salvo.save()
        return super().form_valid(form)
  
class TipoTreinoListView(LoginRequiredMixin,ListView):
    model = TipoTreino
    template_name = "tipotreino/lista_tipo_treino.html"
    context_object_name = "tipos"
    
    def get_queryset(self):
        return TipoTreino.objects.filter(usuario=self.request.user)
    
class TipoTreinoDeleteView(LoginRequiredMixin,DeleteView):
    model = TipoTreino
    template_name = "tipotreino/confirmacao_deletar_tipo_treino.html"
    success_url = reverse_lazy('lista_tipo_treino')
    context_object_name = "tipos"
    
    def get_queryset(self):
        return TipoTreino.objects.filter(usuario=self.request.user)
       
class TipoTreinoUpdateView(LoginRequiredMixin,UpdateView):
    model = TipoTreino
    template_name="form.html"
    form_class= FormTipoTreino
    success_url = reverse_lazy('lista_tipo_treino')
    
    def form_valid(self,form):
        ttreino_salvo = form.save(commit=False)
        ttreino_salvo.usuario = self.request.user
        
        ttreino_salvo.save()
        return super().form_valid(form)
    
    def get_queryset(self):
        return TipoTreino.objects.filter(usuario=self.request.user)
    
            