from django.urls import path
from .views import views
from .views.usuario_views import UsuarioListView, UsuarioDeleteView, UsuarioFormView, UsuarioUpdateView



urlpatterns =[
    path('tipo_treino/', views.TipoTreinoFormView.as_view(), name="tipo_treino"),
    path('exercicio/', views.ExercicioFormView.as_view(), name='exercicio'),
    path('treino/', views.TreinoFormView.as_view(), name='treino'),
    # Urls de usuarios
    path('usuario/', UsuarioListView.as_view(), name='lista_usuario'),
    path('criar_usuario/', UsuarioFormView.as_view(), name='criar_usuario'),
    path('deletar_usuario/<int:pk>', UsuarioDeleteView.as_view(), name='deletar_usuario'),
    path('editar_usuario/<int:pk>', UsuarioUpdateView.as_view(), name='editar_usuario'),
    
]