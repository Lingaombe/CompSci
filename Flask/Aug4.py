from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<int:x>/<y>/<z>")
def home(x,y,z):

	return render_template("Aug4.html", name=y, rollno=x, Class=z)
	
if __name__ == '__main__':
	app.run(debug = True)
