from django.urls import path
from . import views


urlpatterns =[
    path('tipo_treino/', views.TipoTreinoFormView.as_view(), name="tipo_treino"),
    path('exercicio/', views.ExercicioFormView.as_view(), name='exercicio')
]