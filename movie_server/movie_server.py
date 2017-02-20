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
def movie():	
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	if request.method == "POST":
		try:
			# print("try block")
			title = request.form["title"]
			# print(title)	
			query =  "INSERT INTO movies  values (\"{}\")".format( title)
			# print (query)
			cursor.execute( 'INSERT INTO movies values(\"{}\")'.format( title) )
			connection.commit()
			message = "good"
		except:
			connection.rollback()
			message = "no good"
		finally:		
			connection.close()
		return render_template('result.html', message = message)

@app.route('/movies', methods = ['GET'])
def movies():
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	if request.method == "GET":
		try:
			all_movies_cursor = cursor.excecute('SELECT * FROM movies')
			# print( all_movies_cursor )
			# results = all_movies_cursor.fetchall()
		except:
			return "something wrong"
		finally:
			connection.close()
		return jsonify( results)

@app.route('/search', methods = ['POST'])
def search():
	return jsonify("posted to search")
