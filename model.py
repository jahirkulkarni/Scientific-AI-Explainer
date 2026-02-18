from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load Model and Tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Device Setup (MPS for Mac)
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

def get_explanation(term):
    # Prompt ko detail mangne ke liye modify kiya gaya hai
    prompt = f"Explain the scientific term '{term}' in detail with 3 to 4 sentences:"
    
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    
    # Generation settings for longer and better output
    output = model.generate(
        inputs, 
        max_new_tokens=80,        # Isse explanation lambi hogi
        do_sample=True, 
        temperature=0.8,          # Creativity badhane ke liye
        top_k=50, 
        top_p=0.95,
        no_repeat_ngram_size=2,   # Taaki sentences repeat na hon
        pad_token_id=tokenizer.eos_token_id
    )
    
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Sirf generated explanation nikaalne ke liye prompt ko remove karein
    explanation = decoded_output.replace(prompt, "").strip()
    
    return explanation