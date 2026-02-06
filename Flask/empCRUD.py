#create CRUD app for employees: empno, empname, empdept,empdes,empsal

from flask import Flask,request, redirect, url_for, flash,render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'dbhan'

mysql = MySQL(app)
app.secret_key = "abc"


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM dbhan.emp"
    cursor.execute(query)
    data=cursor.fetchall()
    #return str(data)
    #cursor.close()
    return render_template('empindex.html', student=data)
    

@app.route('/add_student', methods =['POST'])
def add_student():
        empno= request.form['empno']
        empname = request.form['empn']
        empdept = request.form['empde']
        empdes = request.form['empd']
        empsal = request.form['emps']
        cursor = mysql.connection.cursor()
        query='INSERT INTO dbhan.emp (empno, empname, empdept,empdes,empsal) VALUES (%s, %s, %s, %s, %s)'
        val=(empno, empname, empdept,empdes,empsal)
        cursor.execute(query,val)
        mysql.connection.commit()
        flash('Employee added successufully')
        return redirect(url_for('index'))
 
@app.route('/edit/<sid>', methods = ['POST', 'GET'])
def get_student(sid):
    cursor = mysql.connection.cursor()
    query='SELECT * FROM dbhan.emp WHERE empno = %s'
    cursor.execute(query,(sid,))
    #cursor.execute('SELECT * FROM db.student1 WHERE sid = %s', (sid))
    data = cursor.fetchall()
    cursor.close()
    print(data[0])
    return render_template('empedit.html', student = data[0])
 
@app.route('/update/<nid>', methods=['POST'])
def update_student(nid):
    if request.method == 'POST':
        #sid = request.form['sid']
        empname = request.form['empn']
        empdept = request.form['empde']
        empdes = request.form['empd']
        empsal = request.form['emps']
        cursor = mysql.connection.cursor()
        query='UPDATE dbhan.emp SET empname=%s, empdept=%s,empdes=%s,empsal=%s where empno=%s'
        cursor.execute(query,(empname, empdept,empdes,empsal,nid))
        flash('Employee Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<nid>', methods = ['POST','GET'])
def delete_student(nid):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM dbhan.emp WHERE empno = {0}'.format(nid))
    #query='DELETE FROM db.student1 WHERE sid = %s'
    #cursor.execute(query,(nid))
    mysql.connection.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('index'))
    
# running application 
if __name__ == '__main__': 
    app.run(debug=True) 
