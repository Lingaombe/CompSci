from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<int:sec>")
def home(sec):
	return render_template("Aug7.html", x=sec)
	
	
if __name__ == '__main__':
	app.run(debug=True)
