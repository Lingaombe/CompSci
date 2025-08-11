from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<int:money>")
def home(money):
	return render_template("Aug8.html", x=money)
	
	
if __name__ == '__main__':
	app.run(debug=True)
