"use strict";
function encontrarMaiorElemento(numeros) {
    if (numeros.length === 0) {
        throw new Error("O array está vazio.");
    }
    let maior = numeros[0];
    for (let i = 1; i < numeros.length; i++) {
        if (numeros[i] > maior) {
            maior = numeros[i];
        }
    }
    return maior;
}
document
    .getElementById("encontrarMaiorForm")
    .addEventListener("submit", function (event) {
    event.preventDefault();
    const numerosInput = document.getElementById("numerosInput");
    const numerosString = numerosInput.value;
    const numeros = numerosString.split(",").map((num) => Number(num.trim()));
    try {
        const maior = encontrarMaiorElemento(numeros);
        document.getElementById("maiorResultado").innerText = `Maior elemento: ${maior}`;
    }
    catch (error) {
        document.getElementById("maiorResultado").innerText = error.message;
    }
    numerosInput.value = "";
});
class Produto {
    constructor(nome, descricao, preco, quantidadeEstoque) {
        this.nome = nome;
        this.descricao = descricao;
        this.preco = preco;
        this.quantidadeEstoque = quantidadeEstoque;
    }
    exibirInformacoes() {
        return `Nome: ${this.nome}, Descrição: ${this.descricao}, Preço: ${this.preco}, Quantidade em estoque: ${this.quantidadeEstoque}`;
    }
}
function adicionarProduto(event) {
    event.preventDefault();
    const nome = document.getElementById("nomeInput")
        .value;
    const descricao = document.getElementById("descricaoInput").value;
    const precoText = document.getElementById("precoInput").value;
    const quantidade = Number(document.getElementById("quantidadeInput").value);
    const preco = parseFloat(precoText.replace(",", "."));
    if (isNaN(preco)) {
        alert("Por favor, insira um valor de preço válido.");
        return;
    }
    const novoProduto = new Produto(nome, descricao, preco, quantidade);
    const produtoList = document.getElementById("produtoList");
    const produtoItem = document.createElement("li");
    produtoItem.innerText = novoProduto.exibirInformacoes();
    produtoList.appendChild(produtoItem);
    document.getElementById("exercicio12").reset();
}
document
    .getElementById("exercicio12")
    .addEventListener("submit", adicionarProduto);
