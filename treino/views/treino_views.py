from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.urls import reverse_lazy
from treino.forms import FormTreino,FormSetTreinoExercicio,FormSetEditarTreinoExercicio
from treino.models import Treino


class TreinoFormView(FormView):
    template_name='formwithformset.html'
    form_class= FormTreino 
    success_url = reverse_lazy('lista_treino')
    formset = FormSetTreinoExercicio()
    
    #adicionar o formset, adicionado ao context do view
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['formset']= FormSetTreinoExercicio()
        return context
   
    #ultima coisa q arrumei ontem 28/10, falta arrumar o else
    def form_valid(self,form):
        
        formset = self.get_form(FormSetTreinoExercicio)
        
        if formset.is_valid():    
            treino_salvo = form.save()
            formset.instance = treino_salvo
            formset.save()                    
            return super().form_valid(form)
        else:
            return self.form_invalid(formset)
        
class TreinoListView(ListView):
    model = Treino
    template_name = "treino/lista_treino.html"
    context_object_name = "treinos"
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        for treino in context['treinos']:
            treino.exercicios = treino.treinoexercicio_set.all()
        return context
    

class TreinoDeleteView(DeleteView):
    model = Treino
    template_name = "treino/confirmacao_deletar_treino.html"
    success_url = reverse_lazy('lista_treino')
    context_object_name = "treinos"


    
class TreinoUpdateView(UpdateView):
    model = Treino
    template_name="formwithformset.html"
    form_class= FormTreino
    success_url = reverse_lazy('lista_treino')
    formset = FormSetEditarTreinoExercicio()
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['formset']= FormSetEditarTreinoExercicio()
        return context
    
    def form_valid(self,form):
        formset = self.get_form(FormSetEditarTreinoExercicio)
        
        if formset.is_valid():    
            treino_salvo = form.save()
            formset.instance = treino_salvo
            formset.save()                    
            return super().form_valid(form)
        else:
            return self.form_invalid(formset)
                