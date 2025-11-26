from flask import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("Nov1.html")
	
@app.route("/info", methods=["POST"])
def info():
	c = request.form["code"]
	n = request.form["name"]
	ca = request.form["cat"]
	d = request.form["desc"]
	dt = request.form["expd"]
	r = request.form["rate"]
	re = request.form["reo"]
	li = [c, n, ca, d, dt, r, re]
	return render_template("Nov11.html", li = li)

if __name__ == '__main__':
	app.run(debug=True)
