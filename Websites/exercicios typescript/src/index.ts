function calcularDobro(numero) {
  console.log("Função calcularDobro:", numero);
  return numero * 2;
}

document
  .getElementById("exercicio1")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Evita o envio do formulário
    const numero = Number(document.getElementById("numeroInput").value);
    console.log("Número fornecido:", numero);
    const dobro = calcularDobro(numero);
    console.log("Dobro calculado:", dobro);
    document.getElementById("resultado").innerText = "O dobro é: " + dobro;
  });

function exibirTexto(user) {
  console.log("Função exibirTexto:", user);
  const divElement = document.getElementById("exercicio2");
  divElement.innerHTML = `<p>Nome: ${user.name}</p><p>Idade: ${user.age}</p><p>E-mail: ${user.email}</p>`;
}

function main() {
  console.log("Função main: iniciada");
  interface User {
    name: string;
    age: number;
    email: string;
  }

  const user = {
    name: prompt("Digite seu nome:"),
    age: Number(prompt("Digite sua idade:")),
    email: prompt("Digite seu e-mail:"),
  };

  console.log("Usuário fornecido:", user);
  exibirTexto(user);
}

main();

class Produto {
  nome;
  preco;
  quantidadeEstoque;

  constructor(nome, preco, quantidadeEstoque) {
    this.nome = nome;
    this.preco = preco;
    this.quantidadeEstoque = quantidadeEstoque;
  }

  exibirInformacoes() {
    return `Nome: ${this.nome}, Preço: ${this.preco}, Quantidade em estoque: ${this.quantidadeEstoque}`;
  }
}

function adicionarProduto(event) {
  event.preventDefault();

  const nome = document.getElementById("nomeInput").value;
  const precoText = document.getElementById("precoInput").value;
  const quantidade = Number(document.getElementById("quantidadeInput").value);

  const preco = parseFloat(precoText.replace(",", "."));

  if (isNaN(preco)) {
    alert("Por favor, insira um valor de preço válido.");
    return;
  }

  const novoProduto = new Produto(nome, preco, quantidade);

  const produtoList = document.getElementById("produtoList");
  const produtoItem = document.createElement("li");
  produtoItem.innerText = novoProduto.exibirInformacoes();
  produtoList.appendChild(produtoItem);

  console.log("Produto adicionado:", novoProduto);
  document.getElementById("exercicio3").reset();
}

document
  .getElementById("exercicio3")
  .addEventListener("submit", adicionarProduto);

function converterParaMaiusculas(texto) {
  console.log("Função converterParaMaiusculas:", texto);
  return texto.toUpperCase();
}

function aplicarConversao(event) {
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
