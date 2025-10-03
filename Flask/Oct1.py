from flask import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('Oct1.html')
	
@app.route("/submitted", methods=["POST"])
def submitted():
	Rollno = request.form.get("roll")
	Name = request.form.get("sname")
	Gend = request.form.get("gender")
	Class = request.form.get("class")
	mk1 = int(request.form.get("marks1"))
	mk2 = int(request.form.get("marks2"))
	mk3 = int(request.form.get("marks3"))
	
	total = (mk1+mk2+mk3)/3
	
	if total < 40:
		Grade = "Fail"
	elif total < 50:
		Grade = "Pass"
	elif total < 60:
		Grade = "Second class"
	elif total < 70:
		Grade = "First class"
	else:
		Grade = "Distinction"
	
	li = [Rollno, Name, Gend, Class, Grade]
	
	return render_template("Oct11.html", li=li)



if __name__ == '__main__':
	app.run(debug=True)
