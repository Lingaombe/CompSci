from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	name = "Hannah"
	vowels = ["a","e","i","o","u"]
	details = {"Rollno.": 8262, "name": name, "class": "B.Sc III"}
	return render_template("Aug2.html", name=name, vowels=vowels, details=details)
	
if __name__ == '__main__':
	app.run(debug = True)
