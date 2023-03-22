/* calculadora que exiba na tela o resultado*/  
function Mostrador(algo) {
    document.getElementById("Teste").innerHTML = algo;
  }
  
  function Calculadora(num1, num2, Chamando_novamente) {
    let sum = num1 + num2;
    Chamando_novamente(sum);
  }
  
  Calculadora(5, 5, Mostrador);
  
//set timeout

setTimeout(myFunction, 5000);

function myFunction() {
  document.getElementById("demo").innerHTML = "Tempo é relativo, beba água...";
}

setTimeout(myFunction, 10000);

function myFunction() {
  document.getElementById("demo").innerHTML = "Vai dormir";
}

setInterval(myFunction, 1000);

function myFunction() {
  let d = new Date();
  document.getElementById("demo2").innerHTML=
  d.getHours() + ":" +
  d.getMinutes() + ":" +
  d.getSeconds() + ":" 
}

setInterval(my2Function, 100)
function my2Function() {
    let d = new Date();
    document.getElementById("demo3").innerHTML=
  d.getMilliseconds();
}
