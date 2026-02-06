#bookMaster: bookID, bookName, Author, Quantity add five records in table
#studentMaster: rollno, name, class add five records in table
#create webapp form as:
#bookID, select bookID from bookMaster using drop down
#rollno, select from SM using dropdown
#issue date use date component
#return date
#fine = id-rd>7(R0.5/day) ... 
#transfer all data to bookTransaction table

from flask import *
from flask_mysql_connector import MySQL
from datetime import datetime


app = Flask(__name__)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_PASSWORD'] = "mysql"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_DB'] = "dbhan"

mysql = MySQL(app)

@app.route('/', methods=["GET","POST"])
def home():
	cursor = mysql.connection.cursor()
	query='SELECT * FROM dbhan.bookMaster'
	cursor.execute(query)
	book = cursor.fetchall()
	print(book)
	
	que='SELECT * FROM dbhan.studentMaster'
	cursor.execute(que)
	student = cursor.fetchall()
	print(student)
	
	d = fine = studentID=bookID= None
	
	if request.method == 'POST':
		studentID = request.form.get('student')
		bookID = request.form.get("book")
		idate = request.form.get('idate')
		rdate = request.form.get('rdate')
		d1 = datetime.strptime(idate,'%Y-%m-%d')
		d2 = datetime.strptime(rdate,'%Y-%m-%d')
		d = (d2-d1).days
	
	if d>7:
		fine = (d-7)*0.5
	else:
		fine = 0
	
	#cur = mysql.connection.cursor()
	#q = 'INSERT INTO dbhan.bookTransaction (studentID,bookID,idate,rdate,fine) VALUES (%,%,%,%,%)'
	#val = (studentID,bookID,idate,rdate,fine)
	#cur.execute(q,val)
	#mysql.connection..commit()
	
	return render_template("bookForm.html", book=book, student=student, fine=fine, d=d)


if __name__ == '__main__':
	app.run(debug=True)
