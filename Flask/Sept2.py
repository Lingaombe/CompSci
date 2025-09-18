from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	li = ['a','e','O','u','p','q','r','R','A']
	liv = ['a','e','i','o','u','A','E','O','I','U']
	return render_template("Sept2.html", li=li, liv=liv)
	
if __name__ == '__main__':
	app.run(debug=True)
