// Load the quiz questions dynamically using AJAX
function loadQuizQuestions() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var quizQuestions = JSON.parse(xhr.responseText);
      // Call a function to display the quiz questions
      displayQuestion(0); // Display the first question
    }
  };
  xhr.open('GET', '/generate_quiz_questions', true);
  xhr.send();
}

// Example function to display a question on the page
function displayQuestion(index) {
  var question = quizQuestions[index].question;
  var answers = quizQuestions[index].answers;
  // Display the question and answers on the page
  // ...
}

// Call the loadQuizQuestions function to load the quiz questions
loadQuizQuestions();
