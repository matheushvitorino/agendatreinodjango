from django.db import models

# Create your models here.
class TipoTreino(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.OneToOneField(TipoTreino, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.nome} de {self.tipo}'
    
    
class Treino(models.Model):
    series ={
        '3':3,
        '4':4,
        '5':4,
        '6':6,
        }
    exercicio = models.ManyToManyField(Exercicio, related_name='treinos' )
    tipo = models.OneToOneField(TipoTreino, on_delete=models.PROTECT)
    series = models.IntegerField(choices=series, default='3')
    repeticoes = models.IntegerField()
    criado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Treino de {self.tipo}'
    
