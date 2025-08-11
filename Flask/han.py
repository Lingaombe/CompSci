from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
	return "<h1>Welcome to flask</h1>"
	
@app.route('/fname')
def fname():
	return "<h2>Hannah</h2>"
	
@app.route('/mname')
def mname():
	return "<h2>Priscilla Nambewe</h2>"
	
@app.route('/lname')
def lname():
	return "<h2>Mngoli</h2>"
	
@app.route('/name')
def name():
	return "<h2>Hannah Priscilla Mngoli Nambewe</h2>"
