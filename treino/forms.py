from django import forms
from .models import TipoTreino,Treino,Exercicio,TreinoExercicio
from django.forms import formset_factory

class FormTipoTreino(forms.Form):
    nome = forms.CharField(max_length=100)
    
    
class FormExercicio(forms.Form):

    #FOR PARA OBTER TODOS OS TIPO_TREINO EM UMA LISTA DE TUPLAS
 
    nome = forms.CharField(max_length=100)
    tipo_de_treino = forms.ModelChoiceField(
        queryset=TipoTreino.objects.all(),
        empty_label=None
        )

    
class FormTreino(forms.Form):
    tipo_de_treino = forms.ModelChoiceField(
        queryset=TipoTreino.objects.all(),
        empty_label=None
        )
    
class FormTreinoExercicio(forms.Form):
    numero_series = [(3, 3), (4, 4), (5, 5), (6, 6)]
    
    exercicio = forms.ModelChoiceField(
        queryset=Exercicio.objects.all(),
        empty_label=None
    )
    
    series = forms.ChoiceField(choices=numero_series,
                               initial=3)
    repeticoes = forms.IntegerField()
    
FormSetTreinoExercicio = formset_factory(
    FormTreinoExercicio,
    can_delete=True,
    extra=4
    )
    

    
    