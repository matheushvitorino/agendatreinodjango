from django.views.generic import DeleteView,ListView,UpdateView,FormView
from django.urls import reverse_lazy
from treino.forms import FormExercicio
from treino.models import Exercicio


class ExercicioFormView(FormView):
    template_name='form.html'
    form_class= FormExercicio
    success_url=reverse_lazy('lista_exercicio')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class ExercicioListView(ListView):
    model = Exercicio
    template_name = 'exercicio/lista_exercicio.html'
    context_object_name = 'exercicios'
    
class ExercicioDeleteView(DeleteView):
    model = Exercicio
    template_name = "exercicio/confirmacao_deletar_exercicio.html"
    success_url = reverse_lazy('lista_exercicio')
    context_object_name = "exercicios"


    
class ExercicioUpdateView(UpdateView):
    model = Exercicio
    template_name="form.html"
    form_class= FormExercicio
    success_url = reverse_lazy('lista_exercicio')