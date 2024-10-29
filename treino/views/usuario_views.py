from datetime import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
from treino.forms import FormUsuario
from django.views.generic import DeleteView,ListView,UpdateView,FormView
from treino.models import Usuario

class UsuarioFormView(FormView):
    template_name="form.html"
    form_class= FormUsuario
    success_url = reverse_lazy('lista_usuario')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class UsuarioListView(ListView):
    model = Usuario
    template_name = "listausuario.html"
    context_object_name = "usuarios"
    
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "confirmacao_deletar_usuario.html"
    success_url = reverse_lazy('lista_usuario')
    
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name="form.html"
    form_class= FormUsuario
    success_url = reverse_lazy('lista_usuario')
    
            