from django import forms
from django.forms import ModelForm
from .models import TipoTreino,Treino,Exercicio,TreinoExercicio
from django.forms import formset_factory
from django.forms.models import inlineformset_factory


    
class FormTipoTreino(ModelForm):
    class Meta:
        model = TipoTreino
        fields = ["nome"]
    
class FormExercicio(ModelForm):
    class Meta:
        model =  Exercicio
        fields = ["nome","tipo"]
        #Forma de  adicionar as escolhas com base no model TipoTreino
        tipo = forms.ModelChoiceField(
            queryset = TipoTreino.objects.all(),
            required=True,
        )
    
class FormTreino(ModelForm):
    class Meta:
        model = Treino
        fields = ["tipo"]
        tipo = forms.ModelChoiceField(
            queryset = TipoTreino.objects.all(),
            required=True,
        )    
    
class FormTreinoExercicio(ModelForm):
    class Meta:
        model = TreinoExercicio
        fields = ["exercicio","series","repeticoes"]
    numero_series = [(3, 3), (4, 4), (5, 5), (6, 6)]
    
    exercicio = forms.ModelChoiceField(
        queryset=Exercicio.objects.all(),
        empty_label=None,
        )
    
    series = forms.ChoiceField(choices=numero_series,
                               initial=3)    

# metodo para adicionar lista de formularios
FormSetTreinoExercicio = inlineformset_factory( Treino, TreinoExercicio,
                                               form=FormTreinoExercicio, extra=1
    )




    
    