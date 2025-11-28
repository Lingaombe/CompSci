#create a table employee, with empID empName dept category basicSalary

#create web app to insert five records in above table
#to display all inserted records in asc order of empID

from flask import *
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_DB'] = "dbhan"
app.config['MYSQL_PASSWORD'] = "mysql"

mysql = MySQL(app)

@app.route('/')
def home():
	cur = mysql.connection.cursor()
	query = 'CREATE TABLE dbhan.employee (empID int, empName varchar(100), dept varchar(100), category varchar(100), basicSalary int);'
	cur.execute(query)
	mysql.connection.commit()
	cus.close()
	return "success" 
	
@app.route('/insert')
def insert():
	cur = mysql.connection.cursor()
	q = 'INSERT INTO dbhan.employee(empID, empName, dept, category, basicSalary) VALUES (%s, %s, %s, %s, %s);'
	val = ((1,"dzina","accounting","A",20000),(2,"dzila","marketing","A",30500),(3,"bakha","accounting","A",12000))
	cur.executemany(q,val)
	mysql.connection.commit()
	cur.close()
	return "successful"

@app.route('/table')
def table():
	cur = mysql.connection.cursor()
	q = 'SELECT * FROM dbhan.employee order by empID'
	cur.execute(q)
	li = cur.fetchall()
	cur.close()	
	return render_template("Nov4.html", li = li)
	
@app.route('/showtables')
def show():
	cur = mysql.connection.cursor()
	q = 'use dbhan;'
	cur.execute(q)
	q = 'show tables;'
	cur.execute(q)
	out = cur.fetchall()
	cur.close
	return str(out)

if __name__ == '__main__':
	app.run(debug=True)
