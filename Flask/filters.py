from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("filters.html", x="abc", y=[10,2,3,4], z="this is morning", a=-10)

if __name__ == '__main__':
	app.run(debug=True)
