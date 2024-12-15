// Sample data for course announcements
const announcements = [
    { title: "Midterm Grades Posted", date: "2023-03-15", content: "Midterm grades for CHN201 have been posted. Please check your student portal." },
    { title: "Essay Deadline Extended", date: "2023-03-10", content: "The deadline for the comparative literature essay has been extended to March 25th." },
    { title: "New Textbook Available", date: "2023-03-05", content: "The new textbook for CHN301 is now available at the university bookstore." }
];

// Sample data for updates
const updates = [
    { title: "New Research Publication", date: "2023-03-20", content: "My latest research on Chinese dialects has been published in the Journal of Linguistics." },
    { title: "Conference Presentation", date: "2023-03-12", content: "I will be presenting at the International Conference on Asian Studies next month." },
    { title: "Student Achievement", date: "2023-03-08", content: "Congratulations to our student, Emily Chen, for winning the national Chinese speech contest!" }
];

// Function to create announcement cards
function createAnnouncementCard(announcement) {
    return `
        <div class="col-md-4 mb-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${announcement.title}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">${announcement.date}</h6>
                    <p class="card-text">${announcement.content}</p>
                </div>
            </div>
        </div>
    `;
}

// Function to create update items
function createUpdateItem(update) {
    return `
        <div class="update-item">
            <i class="fas fa-bullhorn update-icon"></i>
            <div class="update-content">
                <h5 class="update-title">${update.title}</h5>
                <h6 class="update-date">${update.date}</h6>
                <p class="update-text">${update.content}</p>
            </div>
        </div>
    `;
}

// Populate announcements
// const announcementCards = document.getElementById('announcementCards');
// announcements.forEach(announcement => {
//     announcementCards.innerHTML += createAnnouncementCard(announcement);
// });

// Populate updates
const updatesFeed = document.getElementById('updatesFeed');
updates.forEach(update => {
    updatesFeed.innerHTML += createUpdateItem(update);
});

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