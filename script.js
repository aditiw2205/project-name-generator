function sendMessage() {
  const input = document.getElementById('userInput');
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage(userText, 'user');
  input.value = "";

  fetch("http://localhost:5000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userText })
  })
  .then(response => response.json())
  .then(data => {
    appendMessage(data.response, 'bot');
  })
  .catch(err => {
    appendMessage("Oops! Something went wrong.", 'bot');
  });
}