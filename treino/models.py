from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoTreino(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoTreino, on_delete=models.PROTECT,related_name='exercicios')
    
    def __str__(self):
        return f'{self.nome} de {self.tipo}'

   
class Treino(models.Model):
    usuario = models.ForeignKey(User, related_name='treinos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoTreino, on_delete=models.PROTECT)
    criado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Treino {self.nome} de {self.tipo} criado {self.criado}'
    
class TreinoExercicio(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    series = models.IntegerField(choices=[(3, 3), (4, 4), (5, 5), (6, 6)], default=3)
    repeticoes = models.IntegerField()
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE )
    
    def __str__(self):
        return f'Exercicio de {self.exercicio} {self.series}x{self.repeticoes}'
    

    

    
