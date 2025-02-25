document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const notification = document.getElementById('messageNotification');

    function showNotification(message, type) {
        notification.textContent = message;
        notification.className = `alert message-notification alert-${type}`;
        notification.classList.remove('d-none');
        
        setTimeout(() => {
            notification.classList.add('d-none');
        }, 5000);
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = {
            name: form.name.value,
            email: form.email.value,
            subject: form.subject.value,
            message: form.message.value
        };

        try {
            const response = await fetch('/submit-contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (response.ok) {
                showNotification(data.message, 'success');
                form.reset();
            } else {
                showNotification(data.message, 'danger');
            }
        } catch (error) {
            showNotification('An error occurred while sending your message.', 'danger');
        }
    });
});
