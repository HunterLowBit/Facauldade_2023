const form = document.getElementById("login-form");
form.addEventListener("submit", function (event) {
  event.preventDefault(); // previne o envio do formulário

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Verifica as credenciais do usuário
  if (username === "robson" && password === "2402") {
    alert("Login realizado com sucesso!");
    // Adicione aqui o redirecionamento para a página de destino
  } else {
    alert("Nome de usuário ou senha incorretos.");
  }
});
