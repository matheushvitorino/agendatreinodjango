from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic.edit import FormView
from .forms import FormTipoTreino,FormExercicio,FormTreino
from .models import TipoTreino,Exercicio,Treino

# Create your views here.
class TipoTreinoFormView(FormView):
    template_name='form.html'
    form_class= FormTipoTreino
    success_url=HttpResponse('success method ')
    
    def form_valid(self,form):
        nome = form.cleaned_data['nome']
        tipo = TipoTreino(nome=nome)
        tipo.save()
        return super().form_valid(form)
    
class ExercicioFormView(FormView):
    template_name='form.html'
    form_class= FormExercicio
    success_url=HttpResponse('success method ')
    
    def form_valid(self,form):
        nome = form.cleaned_data['nome']
        tipo_id = form.cleaned_data['tipo']
        tipo = get_object_or_404(TipoTreino, id = tipo_id)
        exercicio = Exercicio(tipo=tipo,nome=nome)
        exercicio.save()
        return super().form_valid(form)
    
class TreinoFormView(FormView):
    template_name='form.html'
    form_class= FormTreino 
    success_url = HttpResponse('success method')
    
    def form_valid(self,form):
        tipo_id = form.cleaned_data['tipo']
        exercicio = form.cleaned_data['exercicio']
        series = form.cleaned_data['series']
        repeticoes = form.cleaned_data['repeticoes']
        treino = Treino(exercicio=exercicio,tipo=tipo_id,series=series,repeticoes=repeticoes)
        treino.save()
        return super().form_valid(form)
    

        