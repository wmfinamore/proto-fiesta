from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Processo
from apps.cargos.models import Vinculo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProcessosListView(ListView):
    model = Processo
    context_object_name = 'processos'


class ProcessoCreateView(LoginRequiredMixin, CreateView):
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


class ProcessoUpdateView(LoginRequiredMixin, UpdateView):
    model = Processo
    fields = ['interessado', 'assunto', 'resumo', 'situacao']
    context_object_name = 'processo'
    # Definir a função get_absolute_url no model

    def form_valid(self, form):
        # recupera o formulário enviado no post, antes do commit
        processo = form.save(commit=False)
        # insere o usuario informado no request
        processo.usuario_alteracao = self.request.user
        # Salva o model processo
        processo.save()
        # retornar o fommulário válido para a superclasse
        return super(ProcessoUpdateView, self).form_valid(form)


class ProcessoDeleteView(LoginRequiredMixin, DeleteView):
    model = Processo
    success_url = reverse_lazy('processos_lista')
    context_object_name = 'processo'


class CaixaListVIew(ListView):
    model = Processo
    template_name = 'processos/caixa_postal.html'
    context_object_name = 'caixa'

    # Override do método que define query_set da view
    def get_queryset(self):
        # seleciona as unidades de lotação do vinculo do usuário
        unidade_usuario = Vinculo.objects.get(funcionario=self.request.user)
        """
            retorna os processos cujo nome do último trâmite é igual as unidades
            de lotação do usuário que fez o request
        """
        unidade = unidade_usuario.lotacao.nome
        return Processo.objects.filter(unidade_atual=unidade)
