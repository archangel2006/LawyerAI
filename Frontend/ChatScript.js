// ---------- Global Variables ----------
let selectedLanguage = 'en';
let chatHistory = []; // stores past chat sessions
let currentChat = []; // current session messages

// Load chat history from localStorage if available
function loadChatHistory() {
  const storedHistory = localStorage.getItem("chatHistory");
  if (storedHistory) {
    chatHistory = JSON.parse(storedHistory);
  }
}
loadChatHistory();

// Save chat history to localStorage
function saveChatHistory() {
  localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
}

// ---------- Set Initial Greeting Based on Language ----------
function setInitialGreeting() {
  const greetingElem = document.getElementById("initialGreeting");
  let greetings = {
    hi: "नमस्कार! आज मैं आपका वकील हूँ! मैं आपकी क्या सहायता कर सकता हूँ?",
    mr: "नमस्कार! आज मी तुमचा वकील आहे! मी तुम्हाला कशी मदत करू शकतो?",
    ta: "வணக்கம்! இன்று நான் உங்கள் வழக்கறிஞராக இருப்பேன்! நான் உங்களுக்கு எப்படி உதவ முடியும்?",
    bn: "নমস্কার! আমি আজ আপনার উকিল! আমি কিভাবে আপনাকে সাহায্য করতে পারি?",
    en: "Hello There! I will be your lawyer for today! How can I assist you?"
  };
  document.getElementById("chat-box").innerHTML = `<div class="message ai-message">${greetings[selectedLanguage]}</div>`;
}
setInitialGreeting();

// ---------- Sidebar (Dashboard) Functions ----------
function toggleSidebar() {
  document.getElementById("sidebar").classList.toggle("show");
}

function goHome() {
  if (currentChat.length > 0) {
    chatHistory.push([...currentChat]);
    saveChatHistory();
    currentChat = [];
  }
  setInitialGreeting();
  toggleSidebar();
  window.location.href = "home.html";
}

function newChat() {
  if (currentChat.length > 0) {
    chatHistory.push([...currentChat]);
    saveChatHistory();
  }
  currentChat = [];
  setInitialGreeting();
  toggleSidebar();
}

function showChatHistory() {
  const chatHistoryList = document.getElementById("chatHistoryList");
  chatHistoryList.innerHTML = "";
  if (chatHistory.length === 0) {
    chatHistoryList.textContent = "No previous chats.";
  } else {
    chatHistory.forEach((chat, index) => {
      const chatDiv = document.createElement("div");
      chatDiv.textContent = "Chat " + (index + 1);
      chatDiv.onclick = function () { loadChat(index); };
      chatHistoryList.appendChild(chatDiv);
    });
  }
}

function loadChat(index) {
  currentChat = chatHistory[index];
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML = "";
  currentChat.forEach((msg) => {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message " + (msg.sender === "user" ? "user-message" : "ai-message");
    msgDiv.textContent = msg.text;
    chatBox.appendChild(msgDiv);
  });
  toggleSidebar();
}

function clearChatHistory() {
  chatHistory = [];
  saveChatHistory();
  document.getElementById("chatHistoryList").innerHTML = "No previous chats.";
}

// ---------- Language Change Function ----------
function changeLanguage(lang) {
  selectedLanguage = lang;
  currentChat = [];
  setInitialGreeting();
}

// ---------- Chat Functions ----------
function sendMessage() {
  const inputField = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userText = inputField.value.trim();
  if (!userText) return;
  
  const userMessageDiv = document.createElement("div");
  userMessageDiv.className = "message user-message";
  userMessageDiv.textContent = userText;
  chatBox.appendChild(userMessageDiv);
  currentChat.push({ sender: "user", text: userText });
  inputField.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
  
  const payload = { message: userText, language: selectedLanguage };

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  })
  .then((response) => response.json())
  .then((data) => {
    const aiResponse = data.ai_explanation || "(AI Response)";
    const related = data.related_sections ? "\n\nRelated Legal Sections:\n" + data.related_sections.join("\n") : "";
    const finalResponse = aiResponse + related;
    
    const aiMessageDiv = document.createElement("div");
    aiMessageDiv.className = "message ai-message";
    aiMessageDiv.textContent = finalResponse;
    chatBox.appendChild(aiMessageDiv);
    currentChat.push({ sender: "ai", text: finalResponse });
    chatBox.scrollTop = chatBox.scrollHeight;
  })
  .catch((err) => { console.error(err); });
}

// ---------- Voice-to-Text (Speech Recognition) ----------
function startListening() {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Speech Recognition is not supported in your browser. Please use Google Chrome.");
    return;
  }
  const recognition = new webkitSpeechRecognition();
  const languageMap = { en: "en-IN", hi: "hi-IN", mr: "mr-IN", ta: "ta-IN", bn: "bn-BD" };
  recognition.lang = languageMap[selectedLanguage] || "en-IN";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onresult = function (event) {
    document.getElementById("user-input").value = event.results[0][0].transcript;
  };

  recognition.onerror = function (event) {
    console.error("Speech recognition error", event);
    alert("Speech recognition error: " + event.error);
  };

  recognition.start();
}
