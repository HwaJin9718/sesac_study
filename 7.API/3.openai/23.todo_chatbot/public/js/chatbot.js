document.addEventListener('DOMContentLoaded', initChatbot)

function initChatbot() {
    createChatbotUI();
    registerEventHanders();
}

// 챗봇창 생성
function createChatbotUI() {
    const chatbotHTML = `
    <div class="chatbot-icon" id="chatbotIcon">
        <i class="bi bi-chat-dots-fill"></i>
    </div>

    <div class="chatbot-window" id="chatbotWindow">
        <div class="chatbot-header">
            <span>Chatbot</span>
            <button id="closeChatbot">X</button>
        </div>
        <div class="chatbot-body">
            <div class="chatbot-messages" id="chatbotMessages"></div>
            <div class="chatbot-input-container">
                <input type="text" id="chatbotInput" placeholder="Type a message...">
                <button id="sendMessage">Send</button>
            </div>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', chatbotHTML)
}

function registerEventHanders() {
    const chatbotIcon = document.getElementById('chatbotIcon');
    const chatbotWindow = document.getElementById('chatbotWindow');
    const closeChatbot = document.getElementById('closeChatbot');
    const sendMessage = document.getElementById('sendMessage');
    const chatbotInput = document.getElementById('chatbotInput');

    // 챗봇창 노출
    chatbotIcon.addEventListener('click', () => {
        chatbotIcon.style.display = 'none';
        chatbotWindow.style.display = 'flex';
    });

    // 챗봇창 닫음 -> 아이콘 노출
    closeChatbot.addEventListener('click', () => {
        chatbotWindow.style.display = 'none';
        chatbotIcon.style.display = 'flex';
    });

    // 채팅 보내기
    sendMessage.addEventListener('click', handleUserMessage);
    chatbotInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleUserMessage();
    });
}

// 채팅 보내기 했을 때 처리
async function handleUserMessage() {
    const input = document.getElementById('chatbotInput');
    const message = input.value.trim();

    if (!message) return;

    // 채팅 입력값이 있을 때 addMessage 함수 호출
    addMessage(message, 'user');
    // const botResponse = '[BOT]' + input.value;
    input.value = '';

    const botResponse = await sendMessageToServer(message);
    addMessage(botResponse, 'bot');
}

// 메시지 user bot에 따라 출력
function addMessage(message, sender) {
    const container = document.getElementById('chatbotMessages');

    const messageElement = document.createElement('div');
    messageElement.innerHTML = sender === 'user'
        ? `<i class="bi bi-person"></i> ${message}`
        : `<i class="bi bi-robot"></i> ${message}`
    messageElement.classList.add(sender);

    container.appendChild(messageElement);
    container.scrollTop = container.scrollHeight;
}

const ECHO_MODE = false;

// 실제 bot 대화 받아오는 함수
async function sendMessageToServer(userInput) {
    if (ECHO_MODE) {
        return `Echo: ${userInput}`
    }

    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({userInput})
    })
    const answer = await response.json();
    // console.log('서버응답:', answer.response)

    return answer.response; // 나중에 서버의 응답 변수로 변경해야함!! ECHO_MODE = false
}
