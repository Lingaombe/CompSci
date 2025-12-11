#2. create a web app form as follows
#consumer type dropdown residential, commercial
#consumer number integer
#select type radio button individual, company, organisation
#first name middle last
#uid
#gender dropdown MF Other
#Marital status dd married unmarried
#DOB date component

#create table consumer( c_type varchar(200), c_num int, s_type varchar(200), f_name varchar(200), m_name varchar(200), l_name varchar(200), uid int, gender varchar(200), m_status varchar(200));


from flask import *
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_DB'] = "dbhan"
app.config['MYSQL_PASSWORD'] = "mysql"

mysql = MySQL(app)

@app.route('/')
def form():
	return render_template('mahadis.html')
	
@app.route('/add', methods = ['POST'])
def add():
	if request.method == 'POST':
		dob = request.form["dob"]	
		uid = request.form["uid"]
		ge = request.form["ge"]
		ms = request.form["ms"]
		fn = request.form["fn"]
		mn = request.form["mn"]
		ln = request.form["ln"]
		ct = request.form["ct"]
		cn = request.form["cn"]
		st = request.form["st"]
		li = [dob,uid,ge,ms,fn,mn,ln,ct,cn,st]
		
		cur = mysql.connection.cursor()
		query = 'INSERT INTO dbhan.consumer (c_type, c_num, s_type, f_name, m_name, l_name, uid, gender, m_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		val = (ct,cn,st,fn,mn,ln,uid,ge,ms)
		cur.execute(query, val)
		mysql.connection.commit()
		cur.close()	
		return render_template('mahadis.html')	
		
if __name__ == '__main__':
	app.run(debug=True)
