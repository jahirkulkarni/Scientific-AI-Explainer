from model import get_explanation
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
search_history = []  


users_db = {}

@app.route('/')
def home():
    return redirect(url_for('search'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users_db[username] = password
        return "Registration Successful! <a href='/login'>click here" \
        "</a>"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users_db and users_db[username] == password:
            return f"<h1>Welcome {username}! Login Successful.</h1>"
        else:
            return "<h1>Wrong Details!</h1> <a href='/login'>Try Again</a>"
    return render_template('login.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    explanation = None
    if request.method == 'POST':
        term = request.form.get('term') # User ne jo word dala
        
        # --- YE NAYA HISSA HAI ---
        if term: 
            # Word ko list mein sabse upar add karein
            search_history.insert(0, term) 
        # -------------------------

        explanation = get_ai_explanation(term) # Aapka AI model function
    
    # Ab 'history' ko frontend (HTML) par bhej rahe hain
    return render_template('search.html', explanation=explanation, history=search_history)