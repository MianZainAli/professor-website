// Game logic
const apiKey = 'IriTbQOcW1KZ6JnKA2sCjSy5ZnQGWVhFXcMyMyRs'; // Get from https://quizapi.io/
let currentQuestion = 0;
let score = 0;
let questions = [];

document.getElementById('start-game').addEventListener('click', startGame);
document.getElementById('play-again').addEventListener('click', startGame);

async function startGame() {
    currentQuestion = 0;
    score = 0;
    document.getElementById('score').textContent = score;
    document.getElementById('question-number').textContent = currentQuestion;
    document.getElementById('start-game').style.display = 'none';
    document.getElementById('question-container').style.display = 'block';
    document.getElementById('game-over').style.display = 'none';

    try {
        const response = await fetch('https://quizapi.io/api/v1/questions?apiKey=' + apiKey + '&limit=5&category=code');
        questions = await response.json();
        showQuestion();
    } catch (error) {
        console.error('Error fetching questions:', error);
    }
}

function showQuestion() {
    if (currentQuestion >= 5) {
        gameOver();
        return;
    }

    const question = questions[currentQuestion];
    document.getElementById('question-text').textContent = question.question;
    const answersContainer = document.getElementById('answers-container');
    answersContainer.innerHTML = '';

    Object.entries(question.answers).forEach(([key, value]) => {
        if (value) {
            const button = document.createElement('button');
            button.className = 'answer-btn';
            button.textContent = value;
            button.addEventListener('click', () => checkAnswer(key, question.correct_answers));
            answersContainer.appendChild(button);
        }
    });

    document.getElementById('question-number').textContent = currentQuestion + 1;
}

function checkAnswer(selected, correctAnswers) {
    const correct = correctAnswers[selected + '_correct'] === 'true';
    if (correct) score++;
    document.getElementById('score').textContent = score;
    
    currentQuestion++;            setTimeout(showQuestion, 1000);
}

function gameOver() {
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('game-over').style.display = 'block';
    document.getElementById('final-score').textContent = score;
}