from django.contrib import admin
from .models import TipoTreino,Treino,Exercicio


class TipoTreinoAdmin(admin.ModelAdmin):
    list_display=('nome')
    search_fields=('nome')

class ExercicioAdmin(admin.ModelAdmin)
    list_display=('nome')
    search_fields=('nome')
    
class TreinoAdmin(admin.ModelAdmin):
    list_display=('exercicio','tipo','series','repeticoes')
    search_fields=('tipo','exercicio')
    filter_horizontal=('tipo','exercicio')

admin.site.register(TipoTreino, TipoTreinoAdmin)
admin.site.register(Exercicio, ExercicioAdmin)
admin.site.register(Treino, TreinoAdmin)