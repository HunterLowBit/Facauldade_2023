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
    const nome = document.getElementById("nomeInput").value;
    const descricao = document.getElementById("descricaoInput").value;
    const precoText = document.getElementById("precoInput")
        .value;
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
class Animal {
    constructor(nome, idade, tipo, dono) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
        this.dono = dono;
    }
    exibirInformacoes() {
        return `<li>Nome: ${this.nome}, Idade: ${this.idade}, Tipo: ${this.tipo}, Dono: ${this.dono}</li>`;
    }
}
const animais = [];
function cadastrarAnimal(event) {
    event.preventDefault();
    const nomeInput = document.getElementById("nomeInput");
    const idadeInput = document.getElementById("idadeInput");
    const tipoInput = document.getElementById("tipoInput");
    const donoInput = document.getElementById("donoInput");
    const nome = nomeInput.value;
    const idade = Number(idadeInput.value);
    const tipo = tipoInput.value;
    const dono = donoInput.value;
    const animal = new Animal(nome, idade, tipo, dono);
    animais.push(animal);
    nomeInput.value = "";
    idadeInput.value = "";
    tipoInput.value = "";
    donoInput.value = "";
    exibirListaAnimais();
}
function exibirListaAnimais() {
    const listaAnimais = document.getElementById("listaAnimais");
    listaAnimais.innerHTML = "";
    animais.forEach((animal) => {
        const animalItem = document.createElement("li");
        animalItem.innerHTML = animal.exibirInformacoes();
        listaAnimais.appendChild(animalItem);
    });
}
const animalForm = document.getElementById("animalForm");
animalForm.addEventListener("submit", cadastrarAnimal);
function inverterString(event) {
    event.preventDefault();
    const stringInput = document.getElementById("stringInput");
    const string = stringInput.value;
    const reversedString = reverseString(string);
    const resultElement = document.getElementById("result");
    resultElement.textContent = reversedString;
}
function reverseString(str) {
    return str.split("").reverse().join("");
}
const reverseForm = document.getElementById("reverseForm");
reverseForm.addEventListener("submit", inverterString);
class Livro {
    constructor(titulo, autor, paginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.paginas = paginas;
    }
    exibirInformacoes() {
        return `<li>Título: ${this.titulo}, Autor: ${this.autor}, Páginas: ${this.paginas}</li>`;
    }
}
const livros = [];
function cadastrarLivro(event) {
    event.preventDefault();
    const tituloInput = document.getElementById("tituloInput");
    const autorInput = document.getElementById("autorInput");
    const paginasInput = document.getElementById("paginasInput");
    const titulo = tituloInput.value;
    const autor = autorInput.value;
    const paginas = Number(paginasInput.value);
    const livro = new Livro(titulo, autor, paginas);
    livros.push(livro);
    tituloInput.value = "";
    autorInput.value = "";
    paginasInput.value = "";
    exibirListaLivros();
}
function exibirListaLivros() {
    const listaLivros = document.getElementById("listaLivros");
    listaLivros.innerHTML = "";
    livros.forEach((livro) => {
        const livroItem = document.createElement("li");
        livroItem.innerHTML = livro.exibirInformacoes();
        listaLivros.appendChild(livroItem);
    });
}
const livroForm = document.getElementById("livroForm");
livroForm.addEventListener("submit", cadastrarLivro);
