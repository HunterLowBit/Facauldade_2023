/*implementação de chat gpt com a api key na tela index */
const inputQuestion = document.getElementById("question");
const result = document.getElementById("result");

inputQuestion.addEventListener("keypress", (e)=>{
    if (inputQuestion.value && e.key === "Enter")
        sendQuestion();
});

const OPEN_AI_KEY = "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"

function sendQuestion(){
var sQuestion = inputQuestion.value;

    fetch("https://api.openai.com/v1/completions", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + OPEN_AI_KEY,

        },
        body: JSON.stringify({
            model: "text-davinci-003",
            prompt: sQuestion,
            max_tokens: 2048, //Tamanho da Resposta
            temperature: 0.5, //Criatividade da resposta
        }),

    })
        .then((response) => response.json())
        .then((json) => {
            if (result.value) result.value += "\n"

            if(json.error?.message){
                result.value += `Error: ${json.error.mesage}`        
            } else if (json.choices?.[0].text){
                var text = json.choices[0].text || "Sem Resposta" ;
                result.value += "Chat GPT" + text;
            }
            result.scrollTop = result.scrollHeight;
        })
        .catch((error)=> console.error("Error", error))
        .finally(() => {
            inputQuestion.value = "";
            inputQuestion.disabled = false;
            inputQuestion.focus();
        });

    if (result.value) result.value += "\n\n\n\n";
    result.value += `EU: ${sQuestion}`
    inputQuestion.value = "carregando.....";
    inputQuestion.disabled = true;
    result.scrollTop = result.scrollHeight;

}

   

//fetch openai.com/docs/api?version=latest#text-davinci-003 
//fetch("https://api.openai.com/v1/engines/davinci/completions", {


var instance = M.Carousel.init({
    fullWidth: true,
    indicators: true
  });

 