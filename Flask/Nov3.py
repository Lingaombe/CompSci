#Flask application to create a table, insert records single and multiple records, retrieve records

from flask import *
from flask_mysql_connector import MySQL

app = Flask(__name__)

#configure connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "dbhan"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "mysql"

mysql = MySQL(app)



@app.route('/')
def home():
	query = "create table dbhan.ophunzira(ID int primary key auto_increment not null, name varchar(100), email varchar(100))"
	cursor = mysql.connection.cursor()	
	cursor.execute(query)
	mysql.connection.commit()
	cursor.close()
	return "Table created"
	
@app.route('/insertOne')
def insertOne():
	query = 'insert into dbhan.ophunzira(name,email) values (%s,%s)'
	val = ("hannah","hmn@gmail.com")
	cus = mysql.connection.cursor()
	cus.execute(query,val)
	mysql.connection.commit()
	cus.close()
	return "Value inserted"
	
@app.route('/insertMany')
def insertMany():
	query = 'insert into dbhan.ophunzira(name,email) values (%s,%s)'
	val = (("hannih","hin@outlook.com"),("hanza","hkah@yahoo.com"),("hannz","ghvh@gmail.com"),("halla","hl@hotmail.com"))
	cus = mysql.connection.cursor()
	cus.executemany(query,val)
	mysql.connection.commit()
	cus.close()
	return "Values inserted"
	
@app.route('/retrieveOne')
def retrieveOne():
	query = "select * from dbhan.ophunzira"
	cus = mysql.connection.cursor()
	cus.execute(query)
	disp = cus.fetchone()
	return str(disp)

@app.route('/retrieveAll')
def retrieveAll():
	query = "select * from dbhan.ophunzira order by name"
	cus = mysql.connection.cursor()
	cus.execute(query)
	disp = cus.fetchall()
	return render_template('Nov3.html', d = disp)

if __name__ == '__main__':
	app.run(debug=True)
