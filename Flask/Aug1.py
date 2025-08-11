from flask import Flask

app = Flask(__name__)

app.route("/")
def home():
	x = 50
	return str(x)
	
if __name__ == '__main__':
	app.run(debug = True)
