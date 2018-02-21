from flask import Flask, request, redirect, session, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends_db')

@app.route('/')
def index():
	query = "SELECT name, age, DATE_FORMAT(created_at, '%M, %D') AS date, DATE_FORMAT(created_at, '%Y') AS year FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', friends_list=friends)

@app.route('/add_friend', methods=['POST'])
def add_friend():
	query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
	data = {
			'name': request.form['name'],
			'age': int(request.form['age'])
	}

	mysql.query_db(query, data)

	return redirect('/')
app.run(debug=True)