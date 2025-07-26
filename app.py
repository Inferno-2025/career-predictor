from flask import Flask, render_template, request, redirect, session
from logic import predict_career

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}  # Simulated database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        users[email] = {
            'name': request.form['name'],
            'password': request.form['password']
        }
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None  # default: no error
    if request.method == 'POST':
        email = request.form['email']
        user = users.get(email)
        if user and user['password'] == request.form['password']:
            session['user'] = user['name']
            return redirect('/form')
        else:
            error = "Invalid email or password. Try again."  # 👈 feedback here
    return render_template('login.html', error=error)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if 'user' not in session:
        return redirect('/login')
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    career, reason = predict_career(request.form)
    return render_template('result.html', career=career, reason=reason)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
