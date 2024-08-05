document.addEventListener("DOMContentLoaded", function() {
    const sendButton = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const messages = document.getElementById("messages");

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sendMessage() {
        const userMessage = userInput.value;
        if (userMessage.trim() === "") {
            return;
        }

        // Display the user's message
        const userMessageElement = document.createElement("div");
        userMessageElement.className = "user-message"; // Add class for user messages
        userMessageElement.textContent = userMessage;
        messages.appendChild(userMessageElement);

        // Send the user's message to the server
        fetch('/chatbot/cve_chatbot/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // CSRF token for security
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            const botMessageElement = document.createElement("div");
            botMessageElement.className = "bot-response"; // Add class for bot responses
            botMessageElement.textContent = data.response;
            messages.appendChild(botMessageElement);

            // Clear the input field
            userInput.value = "";

            // Scroll to the bottom
            messages.scrollTop = messages.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Event listener for the send button
    sendButton.addEventListener("click", sendMessage);

    // Event listener for Enter key press
    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});
