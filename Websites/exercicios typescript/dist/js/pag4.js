"use strict";
function encontrarMenorElemento(numeros) {
    if (numeros.length === 0) {
        throw new Error("O array está vazio.");
    }
    let menor = numeros[0];
    for (let i = 1; i < numeros.length; i++) {
        if (numeros[i] < menor) {
            menor = numeros[i];
        }
    }
    return menor;
}
function encontrarMenorElementoHandler(event) {
    event.preventDefault();
    const numerosInput = document.getElementById("numerosInput");
    const numerosString = numerosInput.value;
    const numeros = numerosString.split(",").map((num) => Number(num.trim()));
    try {
        const menor = encontrarMenorElemento(numeros);
        const resultado = document.getElementById("resultado");
        resultado.textContent = `Menor elemento: ${menor}`;
        console.log("Menor elemento encontrado:", menor);
    }
    catch (error) {
        const resultado = document.getElementById("resultado");
        resultado.textContent = error.message;
        console.log("Erro:", error);
    }
    numerosInput.value = "";
}
const menorElementoForm = document.getElementById("menorElementoForm");
menorElementoForm.addEventListener("submit", encontrarMenorElementoHandler);
const funcionarios = [];
function adicionarFuncionario(event) {
    event.preventDefault();
    const nomeInput = document.getElementById("nomeInput");
    const cargoInput = document.getElementById("cargoInput");
    const salarioInput = document.getElementById("salarioInput");
    const nome = nomeInput.value;
    const cargo = cargoInput.value;
    const salario = parseFloat(salarioInput.value);
    const novoFuncionario = { nome, cargo, salario };
    funcionarios.push(novoFuncionario);
    atualizarListaFuncionarios();
    nomeInput.value = "";
    cargoInput.value = "";
    salarioInput.value = "";
    console.log("Funcionário adicionado:", novoFuncionario);
}
function atualizarListaFuncionarios() {
    const listaFuncionarios = document.getElementById("listaFuncionarios");
    // Limpar a lista atual
    while (listaFuncionarios.firstChild) {
        listaFuncionarios.firstChild.remove();
    }
    // Adicionar os funcionários na lista
    for (const funcionario of funcionarios) {
        const funcionarioItem = document.createElement("li");
        funcionarioItem.textContent = `Nome: ${funcionario.nome}, Cargo: ${funcionario.cargo}, Salário: ${funcionario.salario}`;
        listaFuncionarios.appendChild(funcionarioItem);
    }
    console.log("Lista de funcionários atualizada:", funcionarios);
}
const funcionarioForm = document.getElementById("funcionarioForm");
funcionarioForm.addEventListener("submit", adicionarFuncionario);
class Casa {
    constructor(endereco, numeroQuartos, tamanhoTerreno) {
        this.endereco = endereco;
        this.numeroQuartos = numeroQuartos;
        this.tamanhoTerreno = tamanhoTerreno;
    }
    obterInformacoes() {
        return `Endereço: ${this.endereco}, Número de quartos: ${this.numeroQuartos}, Tamanho do terreno: ${this.tamanhoTerreno} metros quadrados.`;
    }
}
const casasCadastradas = [];
function cadastrarCasa(event) {
    event.preventDefault();
    const enderecoInput = document.getElementById("enderecoInput");
    const numeroQuartosInput = document.getElementById("numeroQuartosInput");
    const tamanhoTerrenoInput = document.getElementById("tamanhoTerrenoInput");
    const endereco = enderecoInput.value;
    const numeroQuartos = parseInt(numeroQuartosInput.value);
    const tamanhoTerreno = parseInt(tamanhoTerrenoInput.value);
    const novaCasa = new Casa(endereco, numeroQuartos, tamanhoTerreno);
    casasCadastradas.push(novaCasa);
    exibirCasasCadastradas();
    enderecoInput.value = "";
    numeroQuartosInput.value = "";
    tamanhoTerrenoInput.value = "";
    console.log("Casa cadastrada:", novaCasa);
}
function exibirCasasCadastradas() {
    const casasCadastradasElement = document.getElementById("casasCadastradas");
    casasCadastradasElement.innerHTML = "";
    for (const casa of casasCadastradas) {
        const casaElement = document.createElement("div");
        casaElement.innerHTML = `<p>${casa.obterInformacoes()}</p>`;
        casasCadastradasElement.appendChild(casaElement);
    }
    console.log("Casas cadastradas:", casasCadastradas);
}
const casaForm = document.getElementById("casaForm");
casaForm.addEventListener("submit", cadastrarCasa);
function removerEspacos(str) {
    return str.replace(/\s/g, "");
}
function removerEspacosHandler(event) {
    event.preventDefault();
    const inputElement = document.getElementById("inputString");
    const inputString = inputElement.value;
    const novaString = removerEspacos(inputString);
    const resultadoElement = document.getElementById("resultado1");
    resultadoElement.textContent = `String sem espaços: ${novaString}`;
    inputElement.value = "";
    console.log("String sem espaços:", novaString);
}
const formElement = document.getElementById("removerEspacosForm");
formElement.addEventListener("submit", removerEspacosHandler);
const celulares = [];
function adicionarCelular(event) {
    event.preventDefault();
    const marcaInput = document.getElementById("marcaInput");
    const modeloInput = document.getElementById("modeloInput");
    const soInput = document.getElementById("soInput");
    const capacidadeInput = document.getElementById("capacidadeInput");
    const marca = marcaInput.value;
    const modelo = modeloInput.value;
    const sistemaOperacional = soInput.value;
    const capacidadeArmazenamento = parseInt(capacidadeInput.value);
    const novoCelular = {
        marca,
        modelo,
        sistemaOperacional,
        capacidadeArmazenamento,
    };
    celulares.push(novoCelular);
    atualizarListaCelulares();
    limparFormulario();
    console.log("Celular adicionado:", novoCelular);
}
function atualizarListaCelulares() {
    const listaCelulares = document.getElementById("listaCelulares");
    listaCelulares.innerHTML = "";
    for (const celular of celulares) {
        const li = document.createElement("li");
        li.textContent = `Marca: ${celular.marca}, Modelo: ${celular.modelo}, Sistema Operacional: ${celular.sistemaOperacional}, Capacidade: ${celular.capacidadeArmazenamento} GB`;
        listaCelulares.appendChild(li);
    }
    console.log("Lista de celulares atualizada:", celulares);
}
function limparFormulario() {
    const marcaInput = document.getElementById("marcaInput");
    const modeloInput = document.getElementById("modeloInput");
    const soInput = document.getElementById("soInput");
    const capacidadeInput = document.getElementById("capacidadeInput");
    marcaInput.value = "";
    modeloInput.value = "";
    soInput.value = "";
    capacidadeInput.value = "";
}
const celularForm = document.getElementById("celularForm");
celularForm.addEventListener("submit", adicionarCelular);
