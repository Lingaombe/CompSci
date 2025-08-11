from flask import Flask

app = Flask(__name__)

x=10
y=20

@app.route('/')
def add():
	return "Addition: " + str(x+y)
	
@app.route('/sub')
def sub():
	return "Subtraction: "+str(x-y)
	
@app.route('/multi')
def multi():
	return "Multiplication: "+str(x*y)
	
@app.route('/div')
def div():
	return "Division: "+str(x/y)

