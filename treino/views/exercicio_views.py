from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from treino.forms import FormExercicio
from treino.models import Exercicio

class ExercicioFormView(LoginRequiredMixin,FormView):
    template_name='form.html'
    form_class= FormExercicio
    success_url=reverse_lazy('lista_exercicio')
    
    def form_valid(self,form):
        exercicio_salvo = form.save(commit = False)
        exercicio_salvo.usuario = self.request.user
        exercicio_salvo.save()
        
        return super().form_valid(form)
    
class ExercicioListView(LoginRequiredMixin,ListView):
    model = Exercicio
    template_name = 'exercicio/lista_exercicio.html'
    context_object_name = 'exercicios'
    
    def get_queryset(self):
        return Exercicio.objects.filter(usuario=self.request.user)
    
class ExercicioDeleteView(LoginRequiredMixin,DeleteView):
    model = Exercicio
    template_name = "exercicio/confirmacao_deletar_exercicio.html"
    success_url = reverse_lazy('lista_exercicio')
    context_object_name = "exercicios"
    
    def get_queryset(self):
        return Exercicio.objects.filter(usuario=self.request.user)
   
class ExercicioUpdateView(LoginRequiredMixin,UpdateView):
    model = Exercicio
    template_name="form.html"
    form_class= FormExercicio
    success_url = reverse_lazy('lista_exercicio')
    
    def form_valid(self,form):
        exercicio_salvo = form.save(commit = False)
        exercicio_salvo.usuario = self.request.user
        
        exercicio_salvo.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Exercicio.objects.filter(usuario=self.request.user)