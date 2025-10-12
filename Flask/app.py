from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("index.html", temperature=30, rain="True")
if __name__ == '__main__':
	app.run(debug=True)
