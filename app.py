from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Load credentials from environment variables
expected_username = os.environ.get("USERNAME")
expected_password = os.environ.get("PASSWORD")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == expected_username and password == expected_password:
            return redirect(url_for('welcome'))
        else:
            return "Access denied. Invalid username or password."

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return "Welcome to your personal website!"

if __name__ == '__main__':
    app.run(debug=True)

