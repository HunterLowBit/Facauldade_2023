function converterParaMaiusculas(texto: string): string {
  console.log("Função converterParaMaiusculas:", texto);
  return texto.toUpperCase();
}

function converterPrimeiraLetraCadaPalavra(texto: string): string {
  console.log("Função converterPrimeiraLetraCadaPalavra:", texto);
  return texto
    .toLowerCase()
    .replace(/(?:^|\s)\w/g, (match) => match.toUpperCase());
}

function aplicarConversao(event: Event): void {
  event.preventDefault();
  const texto = (<HTMLTextAreaElement>document.getElementById("textoInput"))
    .value;

  const textoConvertidoMaiusculas = converterParaMaiusculas(texto);
  document.getElementById("resultadoMaiusculas").innerText =
    textoConvertidoMaiusculas;

  const textoConvertidoPrimeiraLetra = converterPrimeiraLetraCadaPalavra(texto);
  document.getElementById("resultadoPrimeiraLetra").innerText =
    textoConvertidoPrimeiraLetra;
}

document
  .getElementById("exercicio4")
  .addEventListener("submit", aplicarConversao);
document
  .getElementById("exercicio5")
  .addEventListener("submit", aplicarConversao);
