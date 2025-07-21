# pip install transformers torch

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load pre-trained model and tokenizer
model_name = "gpt2"  # freely available smaller LLM
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set the prompt (user input)
prompt = input("Please enter you prompt here: ")
input_ids = tokenizer.encode(prompt, return_tensors="pt")
attention_mask = torch.ones_like(input_ids)

# Generate continuation
output = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_length=50,
    num_return_sequences=1,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.9,
    pad_token_id=tokenizer.eos_token_id
)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("=== Generated Text ===")
print(generated_text)