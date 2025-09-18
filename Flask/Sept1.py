from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	li = [1,2,3,4,5]
	di = {'rno':12,'name':'hanza','class':'TY'}
	tup = ('hanza','han','hann')
	return render_template("Sept1.html", li=li, di=di, tup=tup)
	
if __name__ == '__main__':
	app.run(debug=True)
