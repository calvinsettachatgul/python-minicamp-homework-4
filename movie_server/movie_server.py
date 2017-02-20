from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/new', methods = ['GET'])
def new():
	return render_template('new.html')

@app.route('/movie', methods = ['POST'])
def create():	
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	if request.method == "POST":
		try:
			print("try block")
			title = request.form("title")
			cursor.execute("INSERT INTO movies (\"name\"), values(\"{}\")".format( title))
			cursor.commit()
			message = "Record Added"
		except:
			cursor.rollback()
			print("something wrong")
			message = "Something Wrong"
		finally:		
				
			connection.close()
			print("done")
			return render_template('result.html', message = message)

@app.route('/movies')
def movies():
	return jsonify("all the movies")

@app.route('/search', methods = ['POST'])
def search():
	return jsonify("posted to search")
