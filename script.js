function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    if (userInput) {
        // Send the user's message to the server
        fetch('/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Display the response from Gemini API
            displayMessage(data.message);
        });
    }
}

function displayMessage(message) {
    var chatWindow = document.getElementById('chat-window');
    var messageElem = document.createElement('div');
    messageElem.textContent = message;
    chatWindow.appendChild(messageElem);
}