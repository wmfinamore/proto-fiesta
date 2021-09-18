from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Processo
from apps.cargos.models import Vinculo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from .forms import SearchForm


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


class ProcessoDetailView(DetailView):
    model = Processo
    context_object_name = 'processo'


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


class CaixaListView(LoginRequiredMixin, ListView):
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


def processo_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        # results = Processo.objects.filter(interessado__icontains=query).order_by('num_processo')
        results = Processo.objects.annotate(
            similarity=TrigramSimilarity('interessado', query)
        ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request,
                  'processos/search.html',
                  {
                      'form': form,
                      'query': query,
                      'results': results
                  })
