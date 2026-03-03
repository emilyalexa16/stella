const dialogueText = document.getElementById("dialogue-text");

// Use empty array if attribute not found
const messagesAttr = dialogueText.getAttribute("data-messages");
const messages = messagesAttr ? JSON.parse(messagesAttr) : [];

let messageIndex = 0;
let charIndex = 0;

function typeMessage() {
  if (!messages.length || messageIndex >= messages.length) return;

  const currentMessage = messages[messageIndex];

  if (charIndex < currentMessage.length) {
    dialogueText.textContent += currentMessage.charAt(charIndex);
    charIndex++;
    setTimeout(typeMessage, 50);
  } else {
    setTimeout(() => {
      dialogueText.textContent += "\n";
      messageIndex++;
      charIndex = 0;
      typeMessage();
    }, 700);
  }
}

typeMessage();