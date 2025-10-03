from flask import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('Oct2.html')
	
@app.route("/submitted", methods=["POST"])
def submitted():
	Rollno = request.form.get("roll")
	Name = request.form.get("sname")
	Gend = request.form.get("gender")
	Class = request.form.get("class")
	mk1 = request.form.get("marks1")
	mk2 = request.form.get("marks2")
	mk3 = int(request.form.get("marks3"))
	mk4 = int(request.form.get("marks4"))
	
	units = mk4-mk3
	total = units
	Bill = 0
	
	if Class == "res":
	
		if units <= 100:
			Bill = units*4.43
			
		elif units <=300:
			Bill = 100*4.43
			units -= 100
			Bill += units*9.84
			
		elif units <=500:
			Bill = (100*4.43) + (200*9.84)
			units -= 300
			Bill += units*12.83
		
		else:
			Bill = (100*4.43) + (200*9.84) + (200*12.83)
			units -= 500
			Bill += units*14.33
		
		Bill += (total*1.24) + 100
		
	if Class == "com":
	
		if units <= 100:
			Bill = units*7.5
			
		elif units <=300:
			Bill = 100*7.5
			units -= 100
			Bill += units*8
			
		elif units <=500:
			Bill = (100*7.5) + (200*8)
			units -= 300
			Bill += units*10.5
		
		else:
			Bill = (100*7.5) + (200*8) + (200*10.5)
			units -= 500
			Bill += units*12.5
		
		Bill += (total*2) + 500
	
	li = [Rollno, Name, Gend, mk1, mk2, Class, Bill]
	
	return render_template("Oct22.html", li=li)



if __name__ == '__main__':
	app.run(debug=True)
