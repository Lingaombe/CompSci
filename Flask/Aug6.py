from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<float:rad>")
def home(rad):
	return render_template("Aug6.html", x=rad)
	
	
if __name__ == '__main__':
	app.run(debug=True)
