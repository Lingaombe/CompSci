from flask import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("Nov2.html")
	
@app.route("/info", methods=["POST"])
def info():
	p = request.form["code"]
	ad = request.form["add"]
	n = request.form["name"]
	ptel = request.form["pt"]
	ca = request.form["cat"]
	dt = request.form["expd"]
	doc = request.form["dn"]
	dtel = request.form["reo"]
	li = [p,n,ad,ptel,doc,dtel,ca,dt]
	return render_template("Nov22.html", li = li)

if __name__ == '__main__':
	app.run(debug=True)
