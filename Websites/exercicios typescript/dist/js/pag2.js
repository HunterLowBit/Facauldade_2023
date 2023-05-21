"use strict";
class Carro {
    constructor(modelo, ano, cor, velocidadeAtual) {
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
        this.velocidadeAtual = velocidadeAtual;
    }
    acelerar(velocidade) {
        this.velocidadeAtual += velocidade;
    }
    frear() {
        this.velocidadeAtual = 0;
    }
    exibirInformacoes() {
        return `Modelo: ${this.modelo}, Ano: ${this.ano}, Cor: ${this.cor}, Velocidade Atual: ${this.velocidadeAtual} KM/H`;
    }
}
function exibirCarro() {
    const modeloInput = document.getElementById("modeloInput");
    const anoInput = document.getElementById("anoInput");
    const corInput = document.getElementById("corInput");
    const velocidadeInput = document.getElementById("velocidadeInput");
    const modelo = modeloInput.value;
    const ano = Number(anoInput.value);
    const cor = corInput.value;
    const velocidade = Number(velocidadeInput.value);
    const carro = new Carro(modelo, ano, cor, velocidade);
    const resultadoElement = document.getElementById("resultado");
    resultadoElement.innerText = carro.exibirInformacoes();
    console.log("Carro exibido:", carro);
}
document
    .getElementById("exercicio5")
    .addEventListener("submit", function (event) {
    event.preventDefault();
    exibirCarro();
});
function calcularSoma(numeros) {
    return numeros.reduce((acc, num) => acc + num, 0);
}
function exibirResultado(event) {
    event.preventDefault();
    const numerosInput = document.getElementById("numerosInput");
    const numerosString = numerosInput.value;
    const numeros = numerosString.split(",").map((num) => parseInt(num));
    const soma = calcularSoma(numeros);
    const resultadoElement = document.getElementById("resultado1");
    resultadoElement.innerText = `A soma dos números é: ${soma}`;
    console.log("Soma calculada:", soma);
}
document
    .getElementById("exercicio6")
    .addEventListener("submit", exibirResultado);
class Animal {
    constructor(nome, idade, tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }
    exibirInformacoes() {
        return `<li>Nome: ${this.nome}, Idade: ${this.idade}, Tipo: ${this.tipo}</li>`;
    }
}
const animais = [];
function cadastrarAnimal(event) {
    event.preventDefault();
    const nomeInput = document.getElementById("nomeInput");
    const idadeInput = document.getElementById("idadeInput");
    const tipoInput = document.getElementById("tipoInput");
    const nome = nomeInput.value;
    const idade = Number(idadeInput.value);
    const tipo = tipoInput.value;
    const animal = new Animal(nome, idade, tipo);
    animais.push(animal);
    nomeInput.value = "";
    idadeInput.value = "";
    tipoInput.value = "";
    exibirListaAnimais();
    console.log("Animal cadastrado:", animal);
}
function exibirListaAnimais() {
    const listaAnimais = document.getElementById("listaAnimais");
    listaAnimais.innerHTML = "";
    animais.forEach((animal) => {
        const animalItem = document.createElement("li");
        animalItem.innerHTML = animal.exibirInformacoes();
        listaAnimais.appendChild(animalItem);
    });
    console.log("Lista de animais:", animais);
}
const animalForm = document.getElementById("animalForm");
animalForm.addEventListener("submit", cadastrarAnimal);
class Pessoa {
    constructor(nome, idade, endereco) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }
    exibirInformacoes() {
        return `Nome: ${this.nome}, Idade: ${this.idade}, Endereço: ${this.endereco}`;
    }
}
function exibirListaPessoas() {
    const listaPessoas = document.getElementById("pessoasList");
    listaPessoas.innerHTML = "";
    pessoas.forEach((pessoa) => {
        const pessoaItem = document.createElement("li");
        pessoaItem.innerHTML = pessoa.exibirInformacoes();
        listaPessoas.appendChild(pessoaItem);
    });
    console.log("Lista de pessoas:", pessoas);
}
const pessoas = [];
function cadastrarPessoa(event) {
    event.preventDefault();
    const nomeInput = document.getElementById("nomeInputPessoa");
    const idadeInput = document.getElementById("idadeInputPessoa");
    const enderecoInput = document.getElementById("enderecoInputPessoa");
    const nome = nomeInput.value;
    const idade = Number(idadeInput.value);
    const endereco = enderecoInput.value;
    const pessoa = new Pessoa(nome, idade, endereco);
    pessoas.push(pessoa);
    nomeInput.value = "";
    idadeInput.value = "";
    enderecoInput.value = "";
    exibirListaPessoas();
    console.log("Pessoa cadastrada:", pessoa);
}
const cadastroForm = document.getElementById("cadastroForm");
cadastroForm.addEventListener("submit", cadastrarPessoa);
function converterParaMinusculas(texto) {
    return texto.toLowerCase();
}
function aplicarConversao(event) {
    event.preventDefault();
    const texto = document.getElementById("textoInput").value;
    const textoConvertido = converterParaMinusculas(texto);
    document.getElementById("resultadoMinusculas").innerText = textoConvertido;
    console.log("Texto convertido:", textoConvertido);
}
document
    .getElementById("exercicio9")
    .addEventListener("submit", aplicarConversao);
class ContaBancaria {
    constructor(numeroConta, saldo) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.transacoes = [];
    }
    depositar(valor) {
        this.saldo += valor;
        this.transacoes.push(`Depósito de ${valor}`);
    }
    sacar(valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            this.transacoes.push(`Saque de ${valor}`);
        }
        else {
            console.log("Saldo insuficiente");
        }
    }
    exibirExtrato() {
        const extratoList = document.getElementById("extratoList");
        extratoList.innerHTML = `<li>Conta: ${this.numeroConta}</li>`;
        extratoList.innerHTML += `<li>Saldo: R$ ${this.saldo.toFixed(2)}</li>`;
        extratoList.innerHTML += `<li>Transações:</li>`;
        this.transacoes.forEach((transacao) => {
            const item = document.createElement("li");
            item.innerText = transacao;
            extratoList.appendChild(item);
        });
    }
}
const contaForm = document.getElementById("contaForm");
contaForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const numeroConta = document.getElementById("numeroContaInput").value;
    const saldo = parseFloat(document.getElementById("saldoInput").value);
    const conta = new ContaBancaria(numeroConta, saldo);
    conta.exibirExtrato();
    const operacoesForm = document.getElementById("operacoesForm");
    const valorInput = document.getElementById("valorInput");
    const depositoButton = document.getElementById("depositoButton");
    const saqueButton = document.getElementById("saqueButton");
    depositoButton.addEventListener("click", function () {
        const valor = parseFloat(valorInput.value);
        conta.depositar(valor);
        conta.exibirExtrato();
        valorInput.value = "";
    });
    saqueButton.addEventListener("click", function () {
        const valor = parseFloat(valorInput.value);
        conta.sacar(valor);
        conta.exibirExtrato();
        valorInput.value = "";
    });
});
console.log("Código carregado com sucesso!");
