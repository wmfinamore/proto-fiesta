from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, View
from .models import Tramite
from .forms import TramiteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import csv
from datetime import datetime
from apps.core.views import Render
from apps.cargos.models import Vinculo


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


class ExportarTramitesCSV(View):

    def get(self, request, **kwargs):

        # definido o charset para renderização correta dos caractéres especiais latinos
        response = HttpResponse(content_type='text/csv; charset="ISO-8859-1"')
        response['Content-Disposition'] = 'attachment; filename="tramitacoes.csv"'

        # kwargs passa um dicionário com os parâmetros informados na url
        tramites = Tramite.objects.filter(processo=kwargs['pk'])

        writer = csv.writer(response)
        writer.writerow(['Processo', 'Despacho', 'Órgão Destino', 'Data Tramite'])
        for tramite in tramites:
            writer.writerow([tramite.numero_processo,
                             tramite.despacho,
                             tramite.orgao_destino,
                             datetime.strftime(tramite.data_tramite, "%d/%m/%Y %H:%M:%S"),
                             ])
        return response


class TramitesNaoRecebidos(LoginRequiredMixin,
                           View):
    # Gera relatórios os processos tramitados para a unidade do usuário que ainda não foram recebidos.
    def get(self, request):
        vinculos = Vinculo.objects.filter(funcionario=request.user)
        data = []
        # Criar lista para usar os dados no filtro do relatório
        for unidade in vinculos:
            data.append(unidade.lotacao)
        """
            retorna os processos último trâmite é igual as unidades
            de lotação do usuário que fez o request
        """
        tramites = Tramite.objects.filter(data_recebimento=None, orgao_destino__in=data)
        params = {
            'data': datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S"),
            'request': request,
            'tramites': tramites,
        }
        return Render.render('tramitacoes/tramites_nao_recebidos.html', params, 'tramites_para_recebimento')
