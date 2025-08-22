from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<car>/<int:days>')
def rental(car,days):
	return render_template("Aug9.html",x=car,y=days)
	
if __name__ == '__main__':
	app.run(debug=True)
