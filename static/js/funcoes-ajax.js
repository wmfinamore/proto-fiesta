function receberProcesso(id) {
    console.log(id);
    token = document.getElementsByName("csrfmidlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/tramitacoes/receber-processo/' + id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}