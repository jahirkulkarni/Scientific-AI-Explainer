from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)


try:
    pipe = pipeline("text-generation", model="gpt2")
except Exception as e:
    print(f"Model Error: {e}")
    pipe = None


search_history = []

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    term = data.get('term', '').strip()

    if not term or any(char.isdigit() for char in term):
        return jsonify({"status": "error", "message": "Numbers not allowed!"}), 400

    try:
        explanation = "Processing..."
        tags = ["Science", "Research"]

        if pipe:
            prompt = f"The scientific concept of {term} is defined as: "
            res = pipe(prompt, max_new_tokens=100, do_sample=True, temperature=0.6, repetition_penalty=1.2)[0]['generated_text']
            explanation = res.strip()
            words = explanation.split()
            tags = list(set([w.strip(".,!():\"") for w in words if len(w) > 5]))[:4]

        if term.upper() not in search_history:
            search_history.insert(0, term.upper())

        return jsonify({
            "status": "success",
            "term": term.upper(),
            "explanation": explanation,
            "related_terms": tags,
            "history": search_history
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/delete_item', methods=['POST'])
def delete_item():
    global search_history
    data = request.get_json()
    item_to_delete = data.get('item')
    if item_to_delete in search_history:
        search_history.remove(item_to_delete)
    return jsonify({"status": "success", "history": search_history})

@app.route('/delete_history', methods=['POST'])
def delete_history():
    global search_history
    search_history = []
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)