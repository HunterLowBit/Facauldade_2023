"use strict";
/**
 * Classe Carro representa um carro com modelo, ano, cor e velocidade atual.
 */
class Carro {
    /**
     * Cria uma instância da classe Carro.
     * @param {string} modelo - O modelo do carro.
     * @param {number} ano - O ano do carro.
     * @param {string} cor - A cor do carro.
     * @param {number} velocidadeAtual - A velocidade atual do carro em KM/H.
     */
    constructor(modelo, ano, cor, velocidadeAtual) {
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
        this.velocidadeAtual = velocidadeAtual;
    }
    /**
     * Acelera o carro aumentando a velocidade atual.
     * @param {number} velocidade - A velocidade a ser adicionada à velocidade atual.
     * @returns {void}
     */
    acelerar(velocidade) {
        this.velocidadeAtual += velocidade;
    }
    /**
     * Freia o carro, definindo a velocidade atual como 0.
     * @returns {void}
     */
    frear() {
        this.velocidadeAtual = 0;
    }
    /**
     * Retorna uma string com as informações do carro.
     * @returns {string} - As informações do carro.
     */
    exibirInformacoes() {
        return `Modelo: ${this.modelo}, Ano: ${this.ano}, Cor: ${this.cor}, Velocidade Atual: ${this.velocidadeAtual} KM/H`;
    }
}
/**
 * Função para exibir as informações do carro na página HTML.
 * @returns {void}
 */
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
/**
 * Função para calcular a soma de um array de números.
 * @param {number[]} numeros - O array de números.
 * @returns {number} - A soma dos números.
 */
function calcularSoma(numeros) {
    return numeros.reduce((acc, num) => acc + num, 0);
}
/**
 * Função para exibir o resultado da soma na página HTML.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
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
/**
 * Classe Animal representa um animal com nome, idade e tipo.
 */
class Animal {
    /**
     * Cria uma instância da classe Animal.
     * @param {string} nome - O nome do animal.
     * @param {number} idade - A idade do animal.
     * @param {string} tipo - O tipo do animal.
     */
    constructor(nome, idade, tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }
    /**
     * Retorna uma string com as informações do animal formatadas como um item de lista HTML.
     * @returns {string} - As informações do animal formatadas como um item de lista HTML.
     */
    exibirInformacoes() {
        return `<li>Nome: ${this.nome}, Idade: ${this.idade}, Tipo: ${this.tipo}</li>`;
    }
}
const animais = [];
/**
 * Função para cadastrar um animal na lista de animais.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
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
/**
 * Função para exibir a lista de animais na página HTML.
 * @returns {void}
 */
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
/**
 * Classe Pessoa representa uma pessoa com nome, idade e endereço.
 */
class Pessoa {
    /**
     * Cria uma instância da classe Pessoa.
     * @param {string} nome - O nome da pessoa.
     * @param {number} idade - A idade da pessoa.
     * @param {string} endereco - O endereço da pessoa.
     */
    constructor(nome, idade, endereco) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }
    /**
     * Retorna uma string com as informações da pessoa.
     * @returns {string} - As informações da pessoa.
     */
    exibirInformacoes() {
        return `Nome: ${this.nome}, Idade: ${this.idade}, Endereço: ${this.endereco}`;
    }
}
/**
 * Função para exibir a lista de pessoas na página HTML.
 * @returns {void}
 */
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
/**
 * Função para cadastrar uma pessoa na lista de pessoas.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
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
/**
 * Função para converter um texto para letras minúsculas.
 * @param {string} texto - O texto a ser convertido.
 * @returns {string} - O texto convertido para letras minúsculas.
 */
function converterParaMinusculas(texto) {
    return texto.toLowerCase();
}
/**
 * Função para aplicar a conversão para letras minúsculas e exibir o resultado na página HTML.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
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
/**
 * Classe ContaBancaria representa uma conta bancária com número da conta, saldo e transações.
 */
class ContaBancaria {
    /**
     * Cria uma instância da classe ContaBancaria.
     * @param {string} numeroConta - O número da conta.
     * @param {number} saldo - O saldo da conta.
     */
    constructor(numeroConta, saldo) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.transacoes = [];
    }
    /**
     * Realiza um depósito na conta bancária e registra a transação.
     * @param {number} valor - O valor a ser depositado.
     * @returns {void}
     */
    depositar(valor) {
        this.saldo += valor;
        this.transacoes.push(`Depósito de ${valor}`);
    }
    /**
     * Realiza um saque na conta bancária, se houver saldo suficiente, e registra a transação.
     * @param {number} valor - O valor a ser sacado.
     * @returns {void}
     */
    sacar(valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            this.transacoes.push(`Saque de ${valor}`);
        }
        else {
            console.log("Saldo insuficiente");
        }
    }
    /**
     * Retorna uma string com as informações da conta bancária e suas transações.
     * @returns {string} - As informações da conta bancária e suas transações.
     */
    exibirExtrato() {
        let extrato = `Conta: ${this.numeroConta}, Saldo: ${this.saldo}\n`;
        extrato += "Transações:\n";
        this.transacoes.forEach((transacao) => {
            extrato += `${transacao}\n`;
        });
        return extrato;
    }
}
/**
 * Função para realizar uma operação de depósito ou saque na conta bancária e exibir o extrato na página HTML.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
function realizarOperacao(event) {
    event.preventDefault();
    const numeroConta = document.getElementById("numeroContaInput");
    const valorInput = document.getElementById("valorInput");
    const operacaoSelect = document.getElementById("operacaoSelect");
    const conta = encontrarConta(numeroConta.value);
    if (conta) {
        const valor = Number(valorInput.value);
        const operacao = operacaoSelect.value;
        if (operacao === "deposito") {
            conta.depositar(valor);
        }
        else if (operacao === "saque") {
            conta.sacar(valor);
        }
        const extratoElement = document.getElementById("extrato");
        extratoElement.innerText = conta.exibirExtrato();
        console.log("Operação realizada:", operacao, "Valor:", valor);
    }
    else {
        console.log("Conta não encontrada");
    }
}
/**
 * Função para encontrar uma conta bancária na lista de contas.
 * @param {string} numeroConta - O número da conta a ser encontrada.
 * @returns {ContaBancaria | undefined} - A conta bancária encontrada ou undefined se não for encontrada.
 */
function encontrarConta(numeroConta) {
    return contas.find((conta) => conta.numeroConta === numeroConta);
}
const contas = [];
document
    .getElementById("contaForm")
    .addEventListener("submit", realizarOperacao);
