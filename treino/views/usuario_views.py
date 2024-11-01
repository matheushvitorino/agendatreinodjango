from django.urls import reverse_lazy
from treino.forms import FormUsuario
from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.contrib.auth.models import User

class UsuarioFormView(FormView):
    template_name="form.html"
    form_class= FormUsuario
    success_url = reverse_lazy('lista_usuario')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class UsuarioListView(ListView):
    model = User
    template_name = "usuario/lista_usuario.html"
    context_object_name = "usuarios"
    
class UsuarioDeleteView(DeleteView):
    model = User
    template_name = "usuario/confirmacao_deletar_usuario.html"
    success_url = reverse_lazy('lista_usuario')
    
class UsuarioUpdateView(UpdateView):
    model = User
    template_name="form.html"
    form_class= FormUsuario
    success_url = reverse_lazy('lista_usuario')
    
            