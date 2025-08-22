from flask import Flask, render_template

app = Flask(__name__)

@app.route('/shipping/<country>/<float:weight>/<member>')
def rental(country,weight,member):
	return render_template("Aug10.html",c=country,w=weight,m=member)
	
if __name__ == '__main__':
	app.run(debug=True)
