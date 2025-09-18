from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	di = {'number':101,'name':'xyz','basic':100000,'HRA':25000,'DA':50000}
	return render_template("Sept4.html", di=di)
	
if __name__ == '__main__':
	app.run(debug=True)
