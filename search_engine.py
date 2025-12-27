import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- Text Preprocessing --------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# -------------------- Load Documents --------------------
documents = []
doc_names = []

DATA_DIR = "."   # current folder (TAN)

for file in os.listdir(DATA_DIR):
    if file.endswith(".txt"):
        with open(file, "r", encoding="utf-8") as f:
            content = preprocess(f.read())
            documents.append(content)
            doc_names.append(file)

if not documents:
    print("❌ No .txt files found in TAN folder.")
    exit()

# -------------------- Vectorization --------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

doc_vectors = vectorizer.fit_transform(documents)

print("\n🔍 Mini Search Engine Ready!")
print("Type 'exit' to quit\n")

# -------------------- Search Loop --------------------
while True:
    query = input("Enter search query: ").strip()

    if query.lower() == "exit":
        print("👋 Exiting search engine.")
        break

    query = preprocess(query)
    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

    top_indices = similarity_scores.argsort()[-3:][::-1]

    print("\n📄 Top Matching Documents:")
    found = False
    for idx in top_indices:
        if similarity_scores[idx] > 0:
            print(f"{doc_names[idx]}  ->  Score: {similarity_scores[idx]:.4f}")
            found = True

    if not found:
        print("No relevant documents found.")

    print()
