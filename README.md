# 🤖 RAG-Powered Project Intelligence Assistant

## 📌 Overview

The **RAG-Powered Project Intelligence Assistant** is an AI-powered application that enables users to ask questions about project documents and receive context-aware answers using **Retrieval-Augmented Generation (RAG)**.

The system extracts text from project documents, generates vector embeddings, stores them in a **FAISS vector database**, retrieves the most relevant information, and uses a **Large Language Model (LLM)** through the **Groq API** to generate accurate responses.

---

## 🚀 Features

* 📄 Document Parsing and Processing
* 🔍 Semantic Search using FAISS Vector Database
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 AI-powered Question Answering
* 📚 Context-aware Responses from Uploaded Documents
* ⚡ Fast Inference using Groq LLM API
* 🖥️ Interactive User Interface with Streamlit

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **LLM:** Groq API
* **Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** Sentence Transformers
* **Document Processing:** PyPDF2 / PDF Parser
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```text
RAG_Project_Intelligence_Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
├── data/
├── parser/
├── embeddings/
├── vectorstore/
├── output/
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/sharanya200224/RAG-Project.git
```

### Navigate to the project

```bash
cd RAG-Project
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## 🧠 How It Works

1. Upload project documents (PDFs).
2. Extract text from the documents.
3. Split text into chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in a FAISS vector database.
6. User enters a question.
7. Retrieve the most relevant chunks using similarity search.
8. Send retrieved context to the Groq LLM.
9. Generate and display an accurate answer.

---

## 📌 Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* Sentence Transformers
* Groq API
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)

---

## 📈 Future Enhancements

* Support multiple document formats (DOCX, PPTX)
* Chat history and memory
* Multi-user authentication
* Cloud deployment
* Hybrid search (Keyword + Semantic)
* Citation and source highlighting

---

## 👩‍💻 Author

**Sharanya B**

* Python Developer
* Django Developer
* AI/ML Enthusiast

GitHub: https://github.com/sharanya200224

---

## 📜 License

This project is developed for educational and learning purposes. Feel free to use and modify it for academic or personal projects.
