from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient

app = Flask(__name__)


client = InferenceClient(api_key="PASTE_TOKEN_HERE")
search_history = []

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    term = data.get('term', '').strip()
    lang = data.get('lang', 'English')

    try:
        
        prompt = f"Explain the scientific concept of {term} in {lang} language in exactly 5 lines. No bold or stars."
        
        
        response = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta", 
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        
        explanation = response.choices[0].message.content.strip()

        if term.upper() not in search_history:
            search_history.insert(0, term.upper())

        return jsonify({
            "status": "success",
            "term": term.upper(),
            "explanation": explanation,
            "related_terms": [term.lower(), "science", lang.lower()],
            "history": search_history
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "API Busy or Task Error. Please try again."}), 500

@app.route('/delete_item', methods=['POST'])
def delete_item():
    global search_history
    data = request.get_json()
    item_to_delete = data.get('item')
    if item_to_delete in search_history:
        search_history.remove(item_to_delete)
    return jsonify({"status": "success", "history": search_history})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080, debug=True)