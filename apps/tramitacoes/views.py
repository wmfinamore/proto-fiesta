from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Tramite
from .forms import TramiteForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TramitacaoCreateView(LoginRequiredMixin, CreateView):
    model = Tramite
    # declarar os campos que o usuário precisa preencher
    fields = ['orgao_destino', 'despacho', ]

    # Fazendo override do formulário para vincular o trâmite ao processo informado na url
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Precisa passar o id do processo, sendo necessário declarar _id explicitamente
        form.instance.processo_id = self.kwargs['pk'] # como usei class based view, precisa referenciar pk, e não id

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # override form_valid
    def form_valid(self, form):
        # recupera o formulário enviado no post, antes do commit
        tramite = form.save(commit=False)
        # insere o usuario informado no request
        tramite.usuario_tramite = self.request.user
        # Salva o model processo
        tramite.save()
        # retornar o fommulário válido para a superclasse
        return super(TramitacaoCreateView, self).form_valid(form)


class TramitacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tramite
    form_class = TramiteForm
    context_object_name = 'tramite'

    def form_valid(self, form):
        # recupera o formulário enviado no post, antes do commit
        tramite = form.save(commit=False)
        # insere o usuario informado no request
        tramite.usuario_recepcao = self.request.user
        # Salva o model processo
        tramite.save()
        # retornar o fommulário válido para a superclasse
        return super(TramitacaoUpdateView, self).form_valid(form)


class TramitacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tramite
    context_object_name = 'tramite'
