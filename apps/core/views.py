from django.shortcuts import render


def home(request):
    """
    Função que renderiza o template index.html que será usado para modelar nossa home.
    Também retorna um dicionário que, a princípio, trabalhará com os dados do usuário
    logado.
    """
    data = {}
    data['usuario'] = request.user
    # data retorna o objeto usuario no contexto
    return render(request, 'core/index.html', data)
