# from dal import autocomplete
# from django.contrib.auth import get_user_model
#
#
# class FuncionarioAutoComplete(autocomplete.Select2QuerySetView):
#
#     def get_queryset(self):
#         Funcionario = get_user_model()
#         if not self.request.user.is_authenticated:
#             return Funcionario.objects.none()
#
#         qs = Funcionario.objects.all()
#
#         if self.q:
#             qs = qs.filter(first_name__istartswith=self.q)
#
#         return qs
