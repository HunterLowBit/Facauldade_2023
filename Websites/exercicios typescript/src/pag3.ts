/**
 * Função para encontrar o maior elemento em um array de números.
 * @param {number[]} numeros - O array de números.
 * @returns {number} - O maior elemento do array.
 * @throws {Error} - Se o array estiver vazio.
 */
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

    const numerosInput = document.getElementById(
      "numerosInput"
    ) as HTMLInputElement;
    const numerosString = numerosInput.value;
    const numeros = numerosString.split(",").map((num) => Number(num.trim()));

    try {
      const maior = encontrarMaiorElemento(numeros);
      document.getElementById(
        "maiorResultado"
      ).innerText = `Maior elemento: ${maior}`;
    } catch (error) {
      document.getElementById("maiorResultado").innerText = error.message;
    }

    numerosInput.value = "";
  });

/**
 * Classe Produto representa um produto com nome, descrição, preço e quantidade em estoque.
 */
class Produto {
  /**
   * Cria uma instância da classe Produto.
   * @param {string} nome - O nome do produto.
   * @param {string} descricao - A descrição do produto.
   * @param {number} preco - O preço do produto.
   * @param {number} quantidadeEstoque - A quantidade em estoque do produto.
   */
  constructor(nome, descricao, preco, quantidadeEstoque) {
    this.nome = nome;
    this.descricao = descricao;
    this.preco = preco;
    this.quantidadeEstoque = quantidadeEstoque;
  }

  /**
   * Retorna uma string com as informações do produto.
   * @returns {string} - As informações do produto.
   */
  exibirInformacoes() {
    return `Nome: ${this.nome}, Descrição: ${this.descricao}, Preço: ${this.preco}, Quantidade em estoque: ${this.quantidadeEstoque}`;
  }
}

/**
 * Função para adicionar um produto à lista de produtos na página HTML.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
function adicionarProduto(event) {
  event.preventDefault();

  const nome = (document.getElementById("nomeInput") as HTMLInputElement).value;
  const descricao = (
    document.getElementById("descricaoInput") as HTMLInputElement
  ).value;
  const precoText = (document.getElementById("precoInput") as HTMLInputElement)
    .value;
  const quantidade = Number(
    (document.getElementById("quantidadeInput") as HTMLInputElement).value
  );

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

  console.log("Produto adicionado:", novoProduto);
}

document
  .getElementById("exercicio12")
  .addEventListener("submit", adicionarProduto);

/**
 * Classe Animal representa um animal com nome, idade, tipo e dono.
 */
class Animal {
  /**
   * Cria uma instância da classe Animal.
   * @param {string} nome - O nome do animal.
   * @param {number} idade - A idade do animal.
   * @param {string} tipo - O tipo do animal.
   * @param {string} dono - O dono do animal.
   */
  constructor(nome, idade, tipo, dono) {
    this.nome = nome;
    this.idade = idade;
    this.tipo = tipo;
    this.dono = dono;
  }

  /**
   * Retorna uma string com as informações do animal.
   * @returns {string} - As informações do animal.
   */
  exibirInformacoes() {
    return `<li>Nome: ${this.nome}, Idade: ${this.idade}, Tipo: ${this.tipo}, Dono: ${this.dono}</li>`;
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

  const nomeInput = document.getElementById("nomeInput") as HTMLInputElement;
  const idadeInput = document.getElementById("idadeInput") as HTMLInputElement;
  const tipoInput = document.getElementById("tipoInput") as HTMLInputElement;
  const donoInput = document.getElementById("donoInput") as HTMLInputElement;

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
 * Função para inverter uma string.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
function inverterString(event) {
  event.preventDefault();

  const stringInput = document.getElementById(
    "stringInput"
  ) as HTMLInputElement;
  const string = stringInput.value;

  const reversedString = reverseString(string);

  const resultElement = document.getElementById("result");
  resultElement.textContent = reversedString;

  console.log("String invertida:", reversedString);
}

/**
 * Função para inverter uma string.
 * @param {string} str - A string a ser invertida.
 * @returns {string} - A string invertida.
 */
function reverseString(str) {
  return str.split("").reverse().join("");
}

const reverseForm = document.getElementById("reverseForm");
reverseForm.addEventListener("submit", inverterString);

/**
 * Classe Livro representa um livro com título, autor e número de páginas.
 */
class Livro {
  /**
   * Cria uma instância da classe Livro.
   * @param {string} titulo - O título do livro.
   * @param {string} autor - O autor do livro.
   * @param {number} paginas - O número de páginas do livro.
   */
  constructor(titulo, autor, paginas) {
    this.titulo = titulo;
    this.autor = autor;
    this.paginas = paginas;
  }

  /**
   * Retorna uma string com as informações do livro.
   * @returns {string} - As informações do livro.
   */
  exibirInformacoes() {
    return `<li>Título: ${this.titulo}, Autor: ${this.autor}, Páginas: ${this.paginas}</li>`;
  }
}

const livros = [];

/**
 * Função para cadastrar um livro na lista de livros.
 * @param {Event} event - O evento de submit.
 * @returns {void}
 */
function cadastrarLivro(event) {
  event.preventDefault();

  const tituloInput = document.getElementById(
    "tituloInput"
  ) as HTMLInputElement;
  const autorInput = document.getElementById("autorInput") as HTMLInputElement;
  const paginasInput = document.getElementById(
    "paginasInput"
  ) as HTMLInputElement;

  const titulo = tituloInput.value;
  const autor = autorInput.value;
  const paginas = Number(paginasInput.value);

  const livro = new Livro(titulo, autor, paginas);
  livros.push(livro);

  tituloInput.value = "";
  autorInput.value = "";
  paginasInput.value = "";

  exibirListaLivros();

  console.log("Livro cadastrado:", livro);
}

/**
 * Função para exibir a lista de livros na página HTML.
 * @returns {void}
 */
function exibirListaLivros() {
  const listaLivros = document.getElementById("listaLivros");
  listaLivros.innerHTML = "";

  livros.forEach((livro) => {
    const livroItem = document.createElement("li");
    livroItem.innerHTML = livro.exibirInformacoes();
    listaLivros.appendChild(livroItem);
  });

  console.log("Lista de livros:", livros);
}

const livroForm = document.getElementById("livroForm");
livroForm.addEventListener("submit", cadastrarLivro);
