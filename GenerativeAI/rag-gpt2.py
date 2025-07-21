# pip install transformers sentence-transformers faiss-cpu

from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import faiss
import torch

# 1. Sample document corpus
documents = [
    "Python is a popular programming language known for its simplicity and readability.",
    "GPT-2 is a language model developed by OpenAI capable of generating human-like text.",
    "The capital of France is Paris.",
    "Machine learning is a branch of artificial intelligence focused on building systems that learn from data."
]

# 2. Create embeddings for documents using sentence-transformers
embedder = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedder.encode(documents, convert_to_tensor=True)

# 3. Build FAISS index for fast similarity search
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings.cpu().detach().numpy())

# 4. Load GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# 5. Function to retrieve top-k documents
def retrieve(query, k=2):
    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, k)
    return [documents[i] for i in I[0]]


# 6. RAG-style QA
def rag_answer(query):
    context_docs = retrieve(query)
    context = "\n".join(context_docs)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(input_ids)

    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=100,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        pad_token_id=tokenizer.eos_token_id
    )

    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer[len(prompt):].strip()


# 7. Test query
question = "What is GPT-2?"
response = rag_answer(question)
print(f"Q: {question}\nA: {response}")