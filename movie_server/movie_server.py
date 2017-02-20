from flask import Flask, render_template, sqlite3, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
