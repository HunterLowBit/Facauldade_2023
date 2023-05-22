/*
 * Encontra o menor elemento em um array de números.
 * @param {number[]} numeros - O array de números.
 * @returns {number} O menor elemento encontrado.
 * @throws {Error} Se o array estiver vazio.

function encontrarMenorElemento(numeros) {
   Implementação da função...
}


 * Manipulador de evento para encontrar o menor elemento.
 * @param {Event} event - O objeto de evento.

function encontrarMenorElementoHandler(event) {
   Implementação do manipulador de evento...
}


 * Interface para representar um funcionário.
 * @typedef {Object} Funcionario
 * @property {string} nome - O nome do funcionário.
 * @property {string} cargo - O cargo do funcionário.
 * @property {number} salario - O salário do funcionário.



 * Array de funcionários.
 * @type {Funcionario[]}

* const funcionarios = [];


 * Adiciona um novo funcionário.
 * @param {Event} event - O objeto de evento.

function adicionarFuncionario(event) {
   Implementação da função...
}


 * Atualiza a lista de funcionários exibida na interface.

function atualizarListaFuncionarios() {
   Implementação da função...
}


 * Classe para representar uma casa.

class Casa {

   * Cria uma instância de Casa.
   * @param {string} endereco - O endereço da casa.
   * @param {number} numeroQuartos - O número de quartos da casa.
   * @param {number} tamanhoTerreno - O tamanho do terreno em metros quadrados.

  constructor(endereco, numeroQuartos, tamanhoTerreno) {
    Inicialização das propriedades da classe...
  }


   * Obtém as informações da casa formatadas como uma string.
   * @returns {string} As informações da casa.

  obterInformacoes() {
    Implementação do método...
  }
}


 * Array de casas cadastradas.
 * @type {Casa[]}

* const casasCadastradas = [];


 * Cadastra uma nova casa.
 * @param {Event} event - O objeto de evento.

function cadastrarCasa(event) {
   Implementação da função...
}


 * Exibe as casas cadastradas na interface.

function exibirCasasCadastradas() {
   Implementação da função...
}


 * Remove os espaços em uma string.
 * @param {string} str - A string a ser processada.
 * @returns {string} A string sem espaços.

function removerEspacos(str) {
   Implementação da função...
}

 * Manipulador de evento para remover espaços.
 * @param {Event} event - O objeto de evento.

function removerEspacosHandler(event) {
  Implementação do manipulador de evento...
}


 * Interface para representar um celular.
 * @typedef {Object} Celular
 * @property {string} marca - A marca do celular.
 * @property {string} modelo - O modelo do celular.
 * @property {string} sistemaOperacional - O sistema operacional do celular.
 * @property {number} capacidadeArmazenamento - A capacidade de armazenamento em GB do celular.



 * Array de celulares.
 * @type {Celular[]}
 
const celulares = [];


 * Adiciona um novo celular.
 * @param {Event} event - O objeto de evento.

function adicionarCelular(event) {
  Implementação da função...
}


 * Atualiza a lista de celulares exibida na interface.

function atualizarListaCelulares() {
   Implementação da função...
}


 * Limpa os campos do formulário de cadastro de celular.

function limparFormulario() {
   Implementação da função...
}
*/

function encontrarMenorElemento(numeros: number[]): number {
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

function encontrarMenorElementoHandler(event: Event) {
  event.preventDefault();

  const numerosInput = document.getElementById(
    "numerosInput"
  ) as HTMLInputElement;
  const numerosString = numerosInput.value;
  const numeros = numerosString.split(",").map((num) => Number(num.trim()));

  try {
    const menor = encontrarMenorElemento(numeros);
    const resultado = document.getElementById("resultado");
    resultado.textContent = `Menor elemento: ${menor}`;

    console.log("Menor elemento encontrado:", menor);
  } catch (error) {
    const resultado = document.getElementById("resultado");
    resultado.textContent = error.message;

    console.log("Erro:", error);
  }

  numerosInput.value = "";
}

const menorElementoForm = document.getElementById("menorElementoForm");
menorElementoForm.addEventListener("submit", encontrarMenorElementoHandler);

interface Funcionario {
  nome: string;
  cargo: string;
  salario: number;
}

const funcionarios: Funcionario[] = [];

function adicionarFuncionario(event: Event) {
  event.preventDefault();

  const nomeInput = document.getElementById("nomeInput") as HTMLInputElement;
  const cargoInput = document.getElementById("cargoInput") as HTMLInputElement;
  const salarioInput = document.getElementById(
    "salarioInput"
  ) as HTMLInputElement;

  const nome = nomeInput.value;
  const cargo = cargoInput.value;
  const salario = parseFloat(salarioInput.value);

  const novoFuncionario: Funcionario = { nome, cargo, salario };
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
  endereco: string;
  numeroQuartos: number;
  tamanhoTerreno: number;

  constructor(endereco: string, numeroQuartos: number, tamanhoTerreno: number) {
    this.endereco = endereco;
    this.numeroQuartos = numeroQuartos;
    this.tamanhoTerreno = tamanhoTerreno;
  }

  obterInformacoes(): string {
    return `Endereço: ${this.endereco}, Número de quartos: ${this.numeroQuartos}, Tamanho do terreno: ${this.tamanhoTerreno} metros quadrados.`;
  }
}

const casasCadastradas: Casa[] = [];

function cadastrarCasa(event: Event) {
  event.preventDefault();

  const enderecoInput = document.getElementById(
    "enderecoInput"
  ) as HTMLInputElement;
  const numeroQuartosInput = document.getElementById(
    "numeroQuartosInput"
  ) as HTMLInputElement;
  const tamanhoTerrenoInput = document.getElementById(
    "tamanhoTerrenoInput"
  ) as HTMLInputElement;

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

function removerEspacos(str: string): string {
  return str.replace(/\s/g, "");
}

function removerEspacosHandler(event: Event) {
  event.preventDefault();

  const inputElement = document.getElementById(
    "inputString"
  ) as HTMLInputElement;
  const inputString = inputElement.value;

  const novaString = removerEspacos(inputString);

  const resultadoElement = document.getElementById("resultado1");
  resultadoElement.textContent = `String sem espaços: ${novaString}`;

  inputElement.value = "";

  console.log("String sem espaços:", novaString);
}

const formElement = document.getElementById("removerEspacosForm");
formElement.addEventListener("submit", removerEspacosHandler);

interface Celular {
  marca: string;
  modelo: string;
  sistemaOperacional: string;
  capacidadeArmazenamento: number;
}

const celulares: Celular[] = [];

function adicionarCelular(event: Event) {
  event.preventDefault();

  const marcaInput = document.getElementById("marcaInput") as HTMLInputElement;
  const modeloInput = document.getElementById(
    "modeloInput"
  ) as HTMLInputElement;
  const soInput = document.getElementById("soInput") as HTMLInputElement;
  const capacidadeInput = document.getElementById(
    "capacidadeInput"
  ) as HTMLInputElement;

  const marca = marcaInput.value;
  const modelo = modeloInput.value;
  const sistemaOperacional = soInput.value;
  const capacidadeArmazenamento = parseInt(capacidadeInput.value);

  const novoCelular: Celular = {
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
  const marcaInput = document.getElementById("marcaInput") as HTMLInputElement;
  const modeloInput = document.getElementById(
    "modeloInput"
  ) as HTMLInputElement;
  const soInput = document.getElementById("soInput") as HTMLInputElement;
  const capacidadeInput = document.getElementById(
    "capacidadeInput"
  ) as HTMLInputElement;

  marcaInput.value = "";
  modeloInput.value = "";
  soInput.value = "";
  capacidadeInput.value = "";
}

const celularForm = document.getElementById("celularForm");
celularForm.addEventListener("submit", adicionarCelular);
