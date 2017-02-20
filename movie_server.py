from flask import Flask, render_template, sqlite3, request

app = FLask(__name__)

@app.route('/')
def home():
	render_template('home.html')
