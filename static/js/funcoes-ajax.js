function receberProcesso(id) {
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax({
        type: 'POST',
        url: '/tramitacoes/receber-processo/'+id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text(result.mensagem);
        }
    });
}