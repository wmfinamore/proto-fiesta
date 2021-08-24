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
        # seleciona os vínculos do usuário que fez o request
        vinculos = Vinculo.objects.filter(funcionario=self.request.user)
        data = []
        # Criar lista para usar os dados no filtro da "caixa postal"
        for unidade in vinculos:
            data.append(unidade.lotacao.nome)
        """
            retorna os processos cujo nome do último trâmite é igual as unidades
            de lotação do usuário que fez o request
        """
        return Processo.objects.filter(unidade_atual__in=data)
