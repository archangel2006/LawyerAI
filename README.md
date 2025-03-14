# 📜 LawyerAI Chatbot

LawyerAI is an AI-powered legal chatbot that provides legal insights based on **Indian law**. It retrieves legal information from **PDFs** (e.g., Indian Constitution, Court Rulings and Government Acts) and uses **OpenAI's GPT** to provide easy-to-understand summaries.

## 🚀 Features
- **Legal Search**: Finds relevant legal sections from uploaded **PDFs**.
- **AI-Powered Explanations**: Uses **OpenAI API** to summarize legal terms.
- **Natural Language Processing (NLP)**: Smart searches beyond keyword matching.
- **Fast Search**: Utilizes **FAISS** (Facebook AI Similarity Search) for quick results.
- **User-Friendly Chat Interface**: Built with **HTML, JavaScript, and Flask**.

---

## 🛠️ Tech Stack
### **Backend**
- **Python (Flask)** - Web API for chatbot interactions
- **FAISS** - Fast vector search for legal text
- **Sentence-Transformers** - NLP-based semantic search
- **PyMuPDF** - Extracts text from legal PDFs
- **OpenAI API** - Provides AI-generated legal summaries (Optional)

### **Frontend**
- **HTML, CSS, JavaScript** - User interface for chatbot
- **Flask, Fetch API** - Sends user queries to backend

### **Database**
- **FAISS Index** - Stores vector embeddings of legal text for fast retrieval

---

## 🔧 Installation & Setup

### **1️⃣ Install Dependencies**
pip install flask pymupdf faiss-cpu sentence-transformers openai

### 2️⃣ Place Your Legal PDF
Copy **PDF file** (e.g., `indian_constitution.pdf`) into the **same folder** as `chatbot.py`.

### **3️⃣ Run the Backend**
python chatbot.py

### **4️⃣ Open the Chatbot Frontend**
- Open `index.html` in **Google Chrome**.
- Ask legal questions and get AI-powered responses.

---

## 📌 How It Works
1. **PDF Processing**: Extracts text from the legal document.
2. **Vector Search**: Converts text into embeddings and stores them in FAISS.
3. **Query Processing**: When a user asks a question, the chatbot:
   - Finds relevant legal sections from the **PDF**.
   - Uses **OpenAI GPT** to summarize them.
4. **Response Generation**: Returns a **simple legal explanation**.

---

## ⚠️ Troubleshooting
### 🔴 **ModuleNotFoundError**
👉 Run `pip install flask pymupdf faiss-cpu sentence-transformers openai` again.

### 🔴 **PDF Not Found**
👉 Ensure your **PDF is in the same folder** as `chatbot.py` and update `pdf_path`.

---

## 🌟 Future Improvements
- **Upload multiple PDFs dynamically**
- **Smarter AI responses**
- **Multilingual support for Indian languages**

📌 Developed for **Indian legal awareness** ⚖️


