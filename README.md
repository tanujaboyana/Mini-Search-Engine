# 🔍 Mini Search Engine using TF-IDF & Cosine Similarity

A **Python-based mini search engine** that retrieves and ranks text documents based on user queries using **TF-IDF vectorization** and **cosine similarity**, demonstrating core principles of **information retrieval and machine learning**.

---

## 🚀 Project Overview

Search engines form the backbone of modern information systems.  
This project simulates a **simplified document search engine** by transforming text into numerical vectors and ranking documents based on semantic relevance.

> 📌 This project showcases practical understanding of **text processing, vector space models, and similarity-based ranking**.

---

## ✨ Key Features
- 📄 Automatically reads multiple text documents
- 🔎 Accepts real-time user search queries
- 📊 Converts text into TF-IDF feature vectors
- 📐 Computes cosine similarity between query and documents
- 🏆 Ranks documents based on relevance score
- ⚠️ Handles no-match queries gracefully

---

## 🧠 How It Works
1. Documents are vectorized using **TF-IDF**
2. User query is transformed using the same vectorizer
3. **Cosine similarity** is computed between query and documents
4. Documents are ranked in descending order of similarity
5. Top matching documents are displayed with scores

---

## 🛠 Tech Stack
- **Python**
- **scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**
- **Information Retrieval Concepts**

---

## 📂 Project Structure
Mini-Search-Engine/
│── doc1.txt
│── doc2.txt
│── doc3.txt
│── search_engine.py
│── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/tanujaboyana/Mini-Search-Engine.git
cd Mini-Search-Engine


### 2️⃣ Install dependencies
pip install scikit-learn

### 3️⃣ Run the program
python search_engine.py

### 4️⃣ Enter a search query
Enter search query: artificial intelligence


### Sample Output
Enter search query: artificial intelligence
Top Matching Documents:
doc3.txt  ->  Score: 0.3628
doc1.txt  ->  Score: 0.2472
doc2.txt  ->  Score: 0.1267


