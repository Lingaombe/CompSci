from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	li = [2,3,4,25,40,55,100,67,98]
	return render_template("Sept3.html", li=li)
	
if __name__ == '__main__':
	app.run(debug=True)
