function encontrarMaiorElemento(numeros: number[]): number {
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

class Produto {
  nome: string;
  descricao: string;
  preco: number;
  quantidadeEstoque: number;

  constructor(
    nome: string,
    descricao: string,
    preco: number,
    quantidadeEstoque: number
  ) {
    this.nome = nome;
    this.descricao = descricao;
    this.preco = preco;
    this.quantidadeEstoque = quantidadeEstoque;
  }

  exibirInformacoes(): string {
    return `Nome: ${this.nome}, Descrição: ${this.descricao}, Preço: ${this.preco}, Quantidade em estoque: ${this.quantidadeEstoque}`;
  }
}

function adicionarProduto(event: Event) {
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

class Animal {
  nome: string;
  idade: number;
  tipo: string;
  dono: string;

  constructor(nome: string, idade: number, tipo: string, dono: string) {
    this.nome = nome;
    this.idade = idade;
    this.tipo = tipo;
    this.dono = dono;
  }

  exibirInformacoes(): string {
    return `<li>Nome: ${this.nome}, Idade: ${this.idade}, Tipo: ${this.tipo}, Dono: ${this.dono}</li>`;
  }
}

const animais: Animal[] = [];

function cadastrarAnimal(event: Event) {
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

function inverterString(event: Event) {
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

function reverseString(str: string): string {
  return str.split("").reverse().join("");
}

const reverseForm = document.getElementById("reverseForm");
reverseForm.addEventListener("submit", inverterString);

class Livro {
  titulo: string;
  autor: string;
  paginas: number;

  constructor(titulo: string, autor: string, paginas: number) {
    this.titulo = titulo;
    this.autor = autor;
    this.paginas = paginas;
  }

  exibirInformacoes(): string {
    return `<li>Título: ${this.titulo}, Autor: ${this.autor}, Páginas: ${this.paginas}</li>`;
  }
}

const livros: Livro[] = [];

function cadastrarLivro(event: Event) {
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
