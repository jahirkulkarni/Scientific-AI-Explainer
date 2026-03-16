from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Model loading logic
try:
    pipe = pipeline("text-generation", model="gpt2")
except Exception as e:
    pipe = None

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    term = request.form.get('term', '').strip()
    if not term:
        return jsonify({"status": "failed", "error": "No term provided"}), 400

    # Static Related Terms for consistency
    related = ["Science", "Physics", "Chemistry", "Biology"]

    try:
        if pipe:
            prompt = f"Define {term} in science:"
            result = pipe(prompt, max_new_tokens=50, do_sample=True)[0]['generated_text']
            explanation = result.replace(prompt, "").strip()
        else:
            explanation = f"Explanation for {term} is loading..."

        return jsonify({
            "status": "success",
            "term": term.upper(),
            "explanation": explanation,
            "related_terms": related
        })
    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500

if __name__ == '__main__':
    # 'debug=True' is important for auto-reload!
    app.run(host='0.0.0.0', port=8080, debug=True)