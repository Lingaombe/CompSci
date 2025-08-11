from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("Aug5.html", x=10,y=12,z=14)
	
	
if __name__ == '__main__':
	app.run(debug=True)
