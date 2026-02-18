from model import get_explanation
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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
    if request.method == 'POST':
        term = request.form.get('term', '').strip()
        
        
        
        if not term.replace(" ", "").isalpha():
            error_msg = "Error: Please enter only scientific words (A-Z). Numbers are not allowed."
            return render_template('search.html', term=term, explanation=error_msg)
        
       
        explanation = get_explanation(term)
        return render_template('search.html', term=term, explanation=explanation)
    
    return render_template('search.html')

if __name__ == '__main__':
 
    app.run(debug=True, port=8080)