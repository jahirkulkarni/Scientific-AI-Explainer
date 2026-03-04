from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
pipe = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    term = request.form.get('term')
    prompt = f"Scientific Definition: {term} is"
    result = pipe(prompt, max_new_tokens=60, repetition_penalty=1.5, do_sample=True, temperature=0.6)[0]['generated_text']
    clean_result = result.replace(prompt, f"{term} is").strip()
    return jsonify({"term": term, "explanation": clean_result})

if __name__ == '__main__':
    app.run(port=8080, debug=True)