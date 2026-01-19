# ⚖️ LawyerAI — Making Law Simple 

LawyerAI is an AI-powered legal assistant designed to make Indian laws understandable, accessible, and easy to navigate.  
It simplifies complex legal text, retrieves relevant constitutional and statutory sections, and provides clear explanations based on Indian law.

---

## 💫 Features

1. **Semantic Legal Search** : Retrieves legally relevant sections from uploaded PDFs (such as the Constitution of India, acts, and rulings) using NLP-based semantic search rather than simple keyword matching.

2. **AI-Powered Explanations** : Uses GPT/LlamaIndex to convert dense legal content into clear and simple terms.

3. **Vector Search (FAISS)** : Semantic search powered by Sentence Transformers and FAISS for fast, contextual retrieval.

4. **Lightweight Backend** : Flask-based backend with efficient PDF parsing, vector indexing, and response generation.

5. **Clean Chat Interface** : HTML/CSS/JS frontend with:
      - Chat history  
      - Voice-to-text input  
      - Multi-language support (English, Hindi, Marathi, Tamil, Bengali)  
      - Responsive UI  

---

## 🛠️ Tech Stack

### Backend
- Python (Flask)  
- LlamaIndex / GPTVectorStoreIndex  
- FAISS (semantic vector search)
- Sentence-Transformers  
- PyMuPDF (PDF extraction)
- OpenAI API or LlamaIndex (AI explanations)

### Frontend
- HTML  
- CSS  
- JavaScript (Fetch API)

### Indexing / Storage
- FAISS vector index  
- PDF-based document store  

---
## 🏗️ High-Level Architecture (End-to-End Flow)
```
┌────────────────────┐
│   User / Browser   │
│  (Chat Interface)  │
└─────────┬──────────┘
          │  Question
          ▼
┌────────────────────┐
│   Query Handler    │
│  (Flask API Route) │
└─────────┬──────────┘
          │
          │ Embed query
          ▼
┌────────────────────────────┐
│ Sentence Transformer Model │
│  (Query Embedding)         │
└─────────┬──────────────────┘
          │
          │ Vector
          ▼
┌────────────────────────────┐
│        FAISS Index         │
│ (Semantic Similarity Search│
│   over Legal Chunks)       │
└─────────┬──────────────────┘
          │ Top-K chunks
          ▼
┌────────────────────────────┐
│   Relevant Legal Text      │
│ (Sections / Clauses)       │
└─────────┬──────────────────┘
          │
          │ Context
          ▼
┌────────────────────────────┐
│ AI Summary Generator       │
│ (LLM / Rule-based summary) │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────────────┐
│   Response Formatter       │
│ - Simplified explanation   │
│ - Referenced sections      │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────┐
│   Chat Interface   │
│  (Final Answer)    │
└────────────────────┘
```
---
## 📄 Offline / One-Time PDF Processing Pipeline

This happens before queries (or when new PDFs are added):
```
┌────────────────────┐
│   Legal PDF Files  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ PDF Text Extractor │
│   (PyMuPDF)        │
└─────────┬──────────┘
          │ Raw text
          ▼
┌────────────────────┐
│ Text Chunker       │
│ (Fixed / Overlap)  │
└─────────┬──────────┘
          │ Chunks
          ▼
┌────────────────────────────┐
│ Sentence Transformer Model │
│ (Chunk Embeddings)         │
└─────────┬──────────────────┘
          │
          ▼
┌────────────────────┐
│    FAISS Index     │
│ (Vector Storage)   │
└────────────────────┘
```
---

## 📁 Project Structure

```
.
├── Backend
│   ├── chatbot.py
│   ├── indian_constitution.pdf
│   ├── main.py
│   └── requirements.txt
│
├── Frontend
│   ├── Chat.html
│   ├── ChatScript.js
│   ├── ChatStyle.css
│   ├── HomeStyle.css
│   └── index.html
│
├── LICENSE
└── README.md
```
---

## 📦 Installation & Setup

### 1. Install Dependencies
```bash
pip install requirements.txt
```

### 2. Add Legal PDFs
Place your legal document(s) in the project folder, for example:
```bash
./indian_constitution.pdf
```
### 3. Run the Backend
```
python main.py
```

### 4. Run the Frontend

```
index.html
```

---

# 🔍 How It Works

1. **PDF Processing** : Text is extracted from the uploaded legal documents and divided into searchable chunks.

2. Embedding Generation : Each chunk is converted into vector embeddings using Sentence Transformers.

3. **FAISS Indexing** : Embeddings are stored in a FAISS index for fast, semantic retrieval.

4. **Query Handling** : When a user asks a question, the system retrieves the most relevant legal sections.

5. **AI Summary Generation** : Retrieved text is summarized into clear and accessible explanations.

5. **Response Delivery** : The chat interface displays both the simplified explanation and the referenced legal sections.

---

## ⚠️ Troubleshooting

### 🔴 **ModuleNotFoundError**
Run `pip install flask pymupdf faiss-cpu sentence-transformers openai` again.

### 🔴 **PDF Not Found**
Ensure your **PDF is in the same folder** as `chatbot.py` and update `pdf_path`.

---



