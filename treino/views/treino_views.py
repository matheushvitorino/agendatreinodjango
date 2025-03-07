from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from treino.forms import FormTreino,FormSetTreinoExercicio,FormSetEditarTreinoExercicio
from treino.models import Treino,HistoricoTreino
from django.shortcuts import render,get_object_or_404,redirect


class TreinoFormView(LoginRequiredMixin,FormView):
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
        treino_salvo = form.save(commit=False)
        treino_salvo.usuario = self.request.user
        treino_salvo.save()
        
        formset = FormSetTreinoExercicio(self.request.POST, self.request.FILES)
        if formset.is_valid:
            for form_exercicio in formset:
                treino_exercicio = form_exercicio.save(commit=False)
                treino_exercicio.treino = treino_salvo
                treino_exercicio.usuario = self.request.user
                treino_exercicio.save()
                return super().form_valid(form)
        else:
            return self.form_invalid(formset)
        
class TreinoListView(LoginRequiredMixin,ListView):
    model = Treino
    template_name = "treino/lista_treino.html"
    context_object_name = "treinos"
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        for treino in context['treinos']:
            treino.exercicios = treino.treinoexercicio_set.all()
        return context
    
    # permite a visualização apenas ao usuario vinculado
    def get_queryset(self):
        return Treino.objects.filter(usuario=self.request.user)

class TreinoDeleteView(LoginRequiredMixin,DeleteView):
    model = Treino
    template_name = "treino/confirmacao_deletar_treino.html"
    success_url = reverse_lazy('lista_treino')
    context_object_name = "treinos"
    
    def get_queryset(self):
        return Treino.objects.filter(usuario=self.request.user)


    
class TreinoUpdateView(LoginRequiredMixin,UpdateView):
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
            treino_salvo = form.save(commit=False)
            treino_salvo.usuario = self.request.user
            treino_salvo.save()

            formset.instance = treino_salvo
            formset.save()                    
            return super().form_valid(formset)
        else:
            return self.form_invalid(formset)
        
    def get_queryset(self):
        return Treino.objects.filter(usuario=self.request.user)
    
def iniciar_treino(request,pk):
    treino = get_object_or_404(Treino, pk=pk)
    
    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        usuario = request.user
        treino_completo = HistoricoTreino(usuario=usuario,treino=treino,comentario=comentario)
        treino_completo.save()
        return redirect('home')
    return render(request,'treino/Ttreino.html',{'treino':treino})
    
    
                