console.log('hello world quiz')
const url = window.location.href

let questionDict ={}
const questionsText = []
const quizBox = document.getElementById('quiz-box')
const scrollBox = document.getElementById('scrollbox-inner')
const quizForm = document.getElementById('quiz-form')
let previousDiv =

$.ajax({
    type:'GET',
    url:`${url}data`,
    success: function(response){
        const data = response.data
        let questionNumber = 0;
        data.forEach(el => {
            for (const[question, answers] of Object.entries(el)){
                questionDict[question] = answers
                questionsText.push(question)
                quizBox.innerHTML+=`
                <div id="${question}"></div>`
                const container = document.getElementById(question)
                container.innerHTML += `
                <hr>
                <div class ="mb-2">
                  <h1><b>${question}</b></h1>
                </div>
            `
            scrollBox.innerHTML+=`
             <div class ="detailQuestion ${questionNumber+=1}" onclick="detailQuestionClick(this)">
                    <h2 value="${question}">Question ${questionNumber}</h2>
                    <h3 id="questionIsAnswered">Unanswered</h>
             </div>
             <br>

            `
            answers.forEach(answer=>{
              container.innerHTML+=`
              <div>
               <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
               <label for="${question}">${answer}</label>
              </div>`  
            })
            container.innerHTML+=`
             <button type="submit" id="${questionNumber}" class="btn btn-success" onclick="questionIsAnswered(this)">Save</button>`
            container.style.display="none"
            
            }
        });
        
        console.log(questionDict)
        

    },
    error: function(error){
        console.log(error)
    }
})

function detailQuestionClick(divElement) {
    // Get the question text and its corresponding container
    let questionText = divElement.querySelector('h2');
    const button = document.getElementsByClassName('btn btn-succes')[0];

    // Hide all question containers first
    for (var question of questionsText) {
        const container = document.getElementById(question);
        if (container) {
            container.style.display="none"
        }
    }

    // Get the container based on the value attribute of questionText
    const container = document.getElementById(questionText.getAttribute('value'));

    // Apply style changes only if necessary
    if (container) {
        container.style.display="block"
    }


    /* 
    Uncomment the following code if you need to render additional content
    using quizBox.innerHTML
    */
    /*
    quizBox.innerHTML = "";
    quizBox.innerHTML += `
        <hr>
        <div class="mb-2">
            <h1><b>${questionText}</b></h1>
        </div>
    `;
    answerText.forEach(answer => {
        quizBox.innerHTML += `
            <div>
                <input type="radio" class="ans" id="${questionText}-${answer}" name="${questionText}" value="${answer}">
                <label for="${questionText}">${answer}</label>
            </div>`;
    });
    */
}

function questionIsAnswered(divElement){
 const sideDiv = document.getElementsByClassName(divElement.id)
 sideDiv[0].querySelector('h3').innerHTML = "Answered"
}

const csrf = document.getElementsByName('csrfmiddlewaretoken')


function sendData() {
 const data = {}
  data['csrfmiddlewaretoken'] = csrf[0].value
  const elements = [...document.getElementsByClassName('ans')]
  elements.forEach(el=>{
    if(el.checked){
        data[el.name] = el.value
    } else{
        if(!data[el.name]) {
            data[el.name] = null
        }
    }
  })

  $.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
  })
}

document.getElementById('submitQuiz').addEventListener('click', event=>{
    event.preventDefault()
    sendData()

}
)



quizForm.addEventListener('submit', event=>{
    event.preventDefault()
    //questionIsAnswered(this)
    //sendData()
})