from django.contrib import admin
from .models import TipoTreino,Treino,Exercicio,TreinoExercicio,HistoricoTreino

class HistoricoTreino(admin.ModelAdmin):
    list_display = ('treino','termino')
    search_fields=('treino')

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields=('nome',)
    
    
class TipoTreinoAdmin(admin.ModelAdmin):
    list_display=('nome','usuario')
    search_fields=('nome','usuario')


class TreinoExercicioInline(admin.TabularInline):
    model = TreinoExercicio

class ExercicioAdmin(admin.ModelAdmin):
    list_display=('nome','tipo')
    search_fields=('nome',)
    
class TreinoAdmin(admin.ModelAdmin):
    list_display=('nome','tipo')
    search_fields=('nome','tipo','exercicio',)
    inlines = [TreinoExercicioInline]
    
admin.site.register(TipoTreino, TipoTreinoAdmin)
admin.site.register(Exercicio, ExercicioAdmin)
admin.site.register(Treino, TreinoAdmin)
admin.site.register(HistoricoTreino, HistoricoTreinoAdmin)
