from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io


class Home(TemplateView):
    template_name = 'core/index.html'


class Render:

    # decorator que dispensa a instanciação do objeto para chamar a função
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('ISO-8859-1')), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type="application/pdf"
            )
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Erro ao renderizar PDF", status=400)
