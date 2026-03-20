from transformers import pipeline


try:
    print("--- LOADING LOCAL GPT-2 MODEL ---")
    
    generator = pipeline('text-generation', model='gpt2')
    print("--- MODEL LOADED SUCCESSFULLY ---")
except Exception as e:
    print(f"Error loading model: {e}")

def get_explanation(term):
    prompt = f"The scientific explanation of {term} is:"
    
    
    result = generator(
        prompt, 
        max_new_tokens=50, 
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256
    )
    
    return result[0]['generated_text']