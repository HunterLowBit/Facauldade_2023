function converterParaMaiusculas(texto) {
    console.log("Função converterParaMaiusculas:", texto);
    return texto.toUpperCase();
}
function converterPrimeiraLetraCadaPalavra(texto) {
    console.log("Função converterPrimeiraLetraCadaPalavra:", texto);
    return texto
        .toLowerCase()
        .replace(/(?:^|\s)\w/g, function (match) { return match.toUpperCase(); });
}
function aplicarConversao(event) {
    event.preventDefault();
    var texto = document.getElementById("textoInput").value;
    var textoConvertidoMaiusculas = converterParaMaiusculas(texto);
    document.getElementById("resultadoMaiusculas").innerText =
        textoConvertidoMaiusculas;
    var textoConvertidoPrimeiraLetra = converterPrimeiraLetraCadaPalavra(texto);
    document.getElementById("resultadoPrimeiraLetra").innerText =
        textoConvertidoPrimeiraLetra;
}
document
    .getElementById("exercicio4")
    .addEventListener("submit", aplicarConversao);
document
    .getElementById("exercicio5")
    .addEventListener("submit", aplicarConversao);
function copiarResultado(elementId) {
    var resultado = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(resultado);
}
