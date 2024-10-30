from django.urls import path
from treino.views.treino_views import TreinoDeleteView,TreinoListView,TreinoFormView,TreinoUpdateView
from .views.usuario_views import UsuarioListView, UsuarioDeleteView, UsuarioFormView, UsuarioUpdateView
from .views.tipo_treino_views import TipoTreinoDeleteView,TipoTreinoFormView,TipoTreinoListView,TipoTreinoUpdateView
from .views.exercicio_views import ExercicioDeleteView,ExercicioFormView,ExercicioListView,ExercicioUpdateView

urlpatterns =[

    #Urls de Treino
    path('treino/', TreinoListView.as_view(), name="lista_treino"),
    path('criar_treino/', TreinoFormView.as_view(), name='criar_treino'),
    path('deletar_treino/<int:pk>', TreinoDeleteView.as_view(), name='deletar_treino'),
    path('editar_treino/<int:pk>', TreinoUpdateView.as_view(), name='editar_treino'),
    # Urls de usuarios
    path('usuario/', UsuarioListView.as_view(), name='lista_usuario'),
    path('criar_usuario/', UsuarioFormView.as_view(), name='criar_usuario'),
    path('deletar_usuario/<int:pk>', UsuarioDeleteView.as_view(), name='deletar_usuario'),
    path('editar_usuario/<int:pk>', UsuarioUpdateView.as_view(), name='editar_usuario'),
    #Urls de TipoTreino
    path('tipo_treino/', TipoTreinoListView.as_view(), name="lista_tipo_treino"),
    path('criar_tipo_treino/', TipoTreinoFormView.as_view(), name='criar_tipo_treino'),
    path('deletar_tipo_treino/<int:pk>', TipoTreinoDeleteView.as_view(), name='deletar_tipo_treino'),
    path('editar_tipo_treino/<int:pk>', TipoTreinoUpdateView.as_view(), name='editar_tipo_treino'),
    #Urls de Exercicio
    path('exercicio/', ExercicioListView.as_view(), name="lista_exercicio"),
    path('criar_exercicio/', ExercicioFormView.as_view(), name='criar_exercicio'),
    path('deletar_exercicio/<int:pk>', ExercicioDeleteView.as_view(), name='deletar_exercicio'),
    path('editar_exercicio/<int:pk>', ExercicioUpdateView.as_view(), name='editar_exercicio'),
    
]