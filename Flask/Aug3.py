from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<int:x>/<int:y>")
def home(x, y):
	return render_template("Aug3.html", x=x, y=y)
	
if __name__ == '__main__':
	app.run(debug = True)
