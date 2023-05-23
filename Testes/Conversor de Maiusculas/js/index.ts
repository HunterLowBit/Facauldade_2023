function converterParaMaiusculas(texto: string): string {
  console.log("Função converterParaMaiusculas:", texto);
  return texto.toUpperCase();
}

/**
 * Função para aplicar a conversão para maiúsculas em um texto e exibir na página HTML.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
function aplicarConversao(event: Event): void {
  event.preventDefault();
  const texto = document.getElementById("textoInput").value;
  console.log("Texto fornecido:", texto);
  const textoConvertido = converterParaMaiusculas(texto);
  console.log("Texto convertido:", textoConvertido);
  document.getElementById("resultadoMaiusculas").innerText = textoConvertido;
}

document
  .getElementById("exercicio4")
  .addEventListener("submit", aplicarConversao);
