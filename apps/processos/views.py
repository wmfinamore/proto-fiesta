from django.views.generic import ListView, CreateView
from .models import Processo

class ProcessosListView(ListView):
    model = Processo
    context_object_name = 'processos'


class ProcessoCreateView(CreateView):
    model = Processo
    fields = ['interessado', 'assunto', 'resumo', 'situacao']
    success_url = '/processos/'
    success_message = 'Processo foi criado com sucesso!'

    # override form_valid
    def form_valid(self, form):
        # recupera o formulário enviado no post, antes do commit
        processo = form.save(commit=False)
        # insere o usuario informado no request
        processo.usuario_criacao = self.request.user
        # Salva o model processo
        processo.save()
        # retornar o fommulário válido para a superclasse
        return super(ProcessoCreateView, self).form_valid(form)
