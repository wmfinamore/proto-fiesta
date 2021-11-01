from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Tramite
from .forms import TramiteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class TramitacaoCreateView(LoginRequiredMixin,
                           PermissionRequiredMixin,
                           CreateView):
    permission_required = ('tramitacoes.add_tramite')
    permission_denied_message = "Você não tem permissão para tramitar processos"
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
        # Salva o model tramite
        tramite.save()
        # retornar o fommulário válido para a superclasse
        return super(TramitacaoCreateView, self).form_valid(form)


class TramitacaoUpdateView(LoginRequiredMixin,
                           PermissionRequiredMixin,
                           UpdateView):
    permission_required = ('tramitacoes.change_tramite')
    permission_denied_message = "Você não tem permissão para alterar tramitações"
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


class TramitacaoDeleteView(LoginRequiredMixin,
                           PermissionRequiredMixin,
                           DeleteView):
    permission_required = ('tramitacoes.delete_tramite')
    permission_denied_message = "Você não tem permissão para excluir tramitações"
    model = Tramite
    # success_url = reverse_lazy('processo_editar')
    context_object_name = 'tramite'

    # Override do
    def get_success_url(self):
        return reverse_lazy('processo_editar', args=[self.object.processo.id])

    #Override do método delete para validação de regra
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        # validamos se a última tramitação não foi recebida para permitir a exclusão
        if self.object.processo.recepcao is None and self.object.data_recebimento is None:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponse('Tramitação já recebida não pode ser excluída')
