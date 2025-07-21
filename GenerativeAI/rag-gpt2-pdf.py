# pip install PyPDF2 sentence-transformers faiss-cpu transformers torch nltk

"""
Extract text from your PDF resume
Chunk the text into manageable parts
Embed those chunks
Retrieve relevant chunks based on a user query
Generate a GPT-2-based answer using the retrieved context
"""

import PyPDF2
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import faiss
import torch
import nltk

nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize


# === 1. Extract Text from PDF Resume ===
def extract_text_from_pdf(path):
    reader = PyPDF2.PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


resume_text = extract_text_from_pdf("C:/Users/sandesku/Documents/Exp_8.3_Yr_Backend_Engineer_NIT_Bhopal.pdf")  # Replace with your resume path


# === 2. Chunk Resume Text ===
def chunk_text(text, chunk_size=2):
    sentences = sent_tokenize(text)
    return [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]


chunks = chunk_text(resume_text)

# === 3. Create Embeddings ===
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks)

# === 4. Build FAISS Index ===
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# === 5. Load GPT-2 Model ===
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")


# === 6. Define Retrieval and Answering ===
def retrieve_context(query, k=2):
    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, k)
    return [chunks[i] for i in I[0]]


def generate_answer(query):
    context = "\n".join(retrieve_context(query))
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(input_ids)

    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=10,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        pad_token_id=tokenizer.eos_token_id
    )

    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer[len(prompt):].strip()


# === 7. Ask Questions ===
query = "What is my name?"
print(f"Q: {query}")
print("A:", generate_answer(query))
