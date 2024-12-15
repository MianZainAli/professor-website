// Sample notices data
const notices = [
    {
        title: "Exam Schedule Change",
        date: "2023-05-01",
        content: "The final exam for CHN301 has been rescheduled to May 15th, 2023. Please make note of this change.",
        important: true
    },
    {
        title: "Office Hours Update",
        date: "2023-04-28",
        content: "Office hours will be held virtually via Zoom for the next two weeks due to building maintenance.",
        important: false
    },
    {
        title: "Guest Lecture Announcement",
        date: "2023-04-25",
        content: "Dr. Jane Smith from Beijing University will be giving a guest lecture on Modern Chinese Literature on April 20th, 2023.",
        important: false
    },
    {
        title: "Research Assistant Positions Available",
        date: "2023-04-20",
        content: "Looking for graduate students interested in Chinese linguistics research. Applications due by May 30th.",
        important: true
    },
    {
        title: "Summer Course Registration",
        date: "2023-04-15",
        content: "Registration for summer Chinese language courses is now open. Early bird discount available until May 1st.",
        important: false
    }
];

// Function to create notice cards
function createNoticeCard(notice) {
    return `
        <div class="col-md-6 mb-4">
            <div class="card notice-card">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-start">
                        <h5 class="card-title">${notice.title}</h5>
                        ${notice.important ? '<span class="badge bg-danger">Important</span>' : ''}
                    </div>
                    <p class="notice-date mb-2">${notice.date}</p>
                    <p class="card-text">${notice.content}</p>
                </div>
            </div>
        </div>
    `;
}

// Populate notices
const noticeList = document.getElementById('noticeList');
notices.sort((a, b) => new Date(b.date) - new Date(a.date)); // Sort by date
notices.forEach(notice => {
    noticeList.innerHTML += createNoticeCard(notice);
});