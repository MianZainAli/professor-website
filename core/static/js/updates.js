// Extended sample data for updates
const allUpdates = [
    { 
        title: "New Research Publication", 
        date: "2023-03-20", 
        content: "My latest research on Chinese dialects has been published in the Journal of Linguistics. The paper explores the evolution of tonal patterns in various Chinese dialects."
    },
    { 
        title: "Conference Presentation", 
        date: "2023-03-12", 
        content: "I will be presenting at the International Conference on Asian Studies next month. The presentation will focus on modern teaching methodologies in Chinese language education."
    },
    { 
        title: "Student Achievement", 
        date: "2023-03-08", 
        content: "Congratulations to our student, Emily Chen, for winning the national Chinese speech contest! Her dedication and hard work have paid off magnificently."
    },
    { 
        title: "Research Grant Awarded", 
        date: "2023-03-01", 
        content: "Received a prestigious research grant for studying the impact of digital technologies on Chinese language learning."
    },
    { 
        title: "Workshop Announcement", 
        date: "2023-02-25", 
        content: "Organizing a workshop on 'Modern Chinese Literature in the Digital Age' next semester. Details will be announced soon."
    },
    { 
        title: "New Research Publication", 
        date: "2023-03-20", 
        content: "My latest research on Chinese dialects has been published in the Journal of Linguistics. The paper explores the evolution of tonal patterns in various Chinese dialects."
    },
    { 
        title: "Conference Presentation", 
        date: "2023-03-12", 
        content: "I will be presenting at the International Conference on Asian Studies next month. The presentation will focus on modern teaching methodologies in Chinese language education."
    },
    { 
        title: "Student Achievement", 
        date: "2023-03-08", 
        content: "Congratulations to our student, Emily Chen, for winning the national Chinese speech contest! Her dedication and hard work have paid off magnificently."
    },
    { 
        title: "Research Grant Awarded", 
        date: "2023-03-01", 
        content: "Received a prestigious research grant for studying the impact of digital technologies on Chinese language learning."
    },
    { 
        title: "Workshop Announcement", 
        date: "2023-02-25", 
        content: "Organizing a workshop on 'Modern Chinese Literature in the Digital Age' next semester. Details will be announced soon."
    },
    { 
        title: "Conference Presentation", 
        date: "2023-03-12", 
        content: "I will be presenting at the International Conference on Asian Studies next month. The presentation will focus on modern teaching methodologies in Chinese language education."
    },
    { 
        title: "Student Achievement", 
        date: "2023-03-08", 
        content: "Congratulations to our student, Emily Chen, for winning the national Chinese speech contest! Her dedication and hard work have paid off magnificently."
    },
    { 
        title: "Research Grant Awarded", 
        date: "2023-03-01", 
        content: "Received a prestigious research grant for studying the impact of digital technologies on Chinese language learning."
    },
    { 
        title: "Workshop Announcement", 
        date: "2023-02-25", 
        content: "Organizing a workshop on 'Modern Chinese Literature in the Digital Age' next semester. Details will be announced soon."
    }
];

// Variables for pagination
const itemsPerPage = 5;
let currentPage = 1;

// Function to create update items
function createUpdateItem(update) {
    return `
        <div class="update-item">
            <h3 class="update-title">${update.title}</h3>
            <div class="update-date">
                <i class="far fa-calendar-alt me-2"></i>${update.date}
            </div>
            <div class="update-content">
                ${update.content}
            </div>
        </div>
    `;
}

// Function to show updates for current page
function showUpdates() {
    const startIndex = 0;
    const endIndex = currentPage * itemsPerPage;
    const updatesFeed = document.getElementById('allUpdatesFeed');
    
    // Clear existing content
    updatesFeed.innerHTML = '';
    
    // Show updates for current page
    allUpdates.slice(startIndex, endIndex).forEach(update => {
        updatesFeed.innerHTML += createUpdateItem(update);
    });

    // Hide "See More" button if all items are shown
    const seeMoreBtn = document.getElementById('seeMoreBtn');
    if (endIndex >= allUpdates.length) {
        seeMoreBtn.style.display = 'none';
    }
}

// Add click event for "See More" button
document.getElementById('seeMoreBtn').addEventListener('click', () => {
    currentPage++;
    showUpdates();
});

// Initial load
showUpdates();