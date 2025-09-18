from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	di = {'number':100,'name':'xyz','grade':'A','basic':50000}
	return render_template("Sept5.html", di=di)
	
if __name__ == '__main__':
	app.run(debug=True)
