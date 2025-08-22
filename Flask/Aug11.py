from flask import Flask, render_template

app = Flask(__name__)

@app.route('/finalResult/<int:marks>/<int:attempt>/<cat>')
def home(marks,attempt,cat):
	return render_template("Aug11.html", m=marks, a=attempt, c=cat)
	
if __name__ == '__main__':
	app.run(debug=True)
