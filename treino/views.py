from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic.edit import FormView
from .forms import FormTipoTreino,FormExercicio,FormTreino, FormSetTreinoExercicio
from .models import TipoTreino,Exercicio,Treino,TreinoExercicio

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
        tipo = form.cleaned_data['tipo']
        exercicio = Exercicio(tipo=tipo,nome=nome)
        exercicio.save()
        return super().form_valid(form)
    
class TreinoFormView(FormView):
    template_name='formwithformset.html'
    form_class= FormTreino 
    success_url = HttpResponse('<p> succes method </p>')
    formset = FormSetTreinoExercicio()
    
    #adicionar o formset, adicionado ao context do view
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['formset']= FormSetTreinoExercicio()
        return context
   
    #ultima coisa q arrumei ontem 28/10, falta arrumar o else
    def form_valid(self,form):
        
        formset = self.get_form(FormSetTreinoExercicio)
        
        if form.is_valid() and formset.is_valid():    
            treino_salvo = form.save()
            formset.instance = treino_salvo
            formset.save()                    
            return super().form_valid(form)
        else:
            return self.form_invalid(formset)
            




    

        