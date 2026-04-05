const form = document.getElementById('prompt-form');
const input = document.querySelector('.prompt-input');
const messages = document.getElementById('chat-messages');
const themeBtn = document.getElementById('theme-toggle-btn');
const deleteBtn = document.getElementById('delete-chats-btn');

// Toggle Dark Mode
themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    themeBtn.textContent = document.body.classList.contains('dark') ? 'dark_mode' : 'light_mode';
});

// Delete Chats
deleteBtn.addEventListener('click', () => {
    if (confirm("Are you sure you want to clear all chats?")) {
        messages.innerHTML = '';
    }
});

// Send Message
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;

    addMessage('user', text);
    input.value = '';

    // Simulate bot reply
    setTimeout(() => {
        addMessage('bot', "Gemini-Orion-Bot says: I'm still learning, but here's a response to '" + text + "'");
    }, 800);
});

// Add Message Function
function addMessage(sender, text) {
    const li = document.createElement('li');
    li.className = sender;
    li.textContent = text;
    messages.appendChild(li);
    messages.scrollTop = messages.scrollHeight;
}
