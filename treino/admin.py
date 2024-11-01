from django.contrib import admin
from .models import TipoTreino,Treino,Exercicio,TreinoExercicio

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields=('nome',)
    
    
class TipoTreinoAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields=('nome',)


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
