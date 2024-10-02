from django import forms
from .models import TipoTreino,Treino,Exercicio

class FormTipoTreino(forms.Form):
    nome = forms.CharField(max_length=100)
    
    
class FormExercicio(forms.Form):
    tipo_treino = TipoTreino.objects.all()
    #FOR PARA OBTER TODOS OS TIPO_TREINO EM UMA LISTA DE TUPLAS
    lista_tipo_treino = [
        (tipo.id,tipo.nome) 
        for tipo in tipo_treino
        ]   
    nome = forms.CharField(max_length=100)
    tipo = forms.ChoiceField(choices=lista_tipo_treino)
    
class FormTreino(forms.Form):
    tipo_treino = TipoTreino.objects.all()
    lista_tipo_treino = [
        (tipo.id,tipo.nome)
        for tipo in tipo_treino
    ]
    exercicios = Exercicio.objects.all()
    lista_exercicios = [
        (exercicio.id, exercicio.nome)
        for exercicio in exercicios
    ]
    
    