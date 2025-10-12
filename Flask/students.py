from flask import *
app = Flask(__name__)
students = {
    101: {"name": "Eliza", "course": "B.Sc CS", "marks": {"Math": 90, "Python": 85, "DBMS": 88}},
    102: {"name": "Cathy", "course": "BCA", "marks": {"Math": 78, "Python": 80, "DBMS": 75}},
    103: {"name": "Ireen", "course": "B.Tech IT", "marks": {"Math": 88, "Python": 92, "DBMS": 95}}
}
@app.route('/student')
def studen():
    studentList = "".join([f"<li>{roll}: {details['name']}</li>" for roll, details in students.items()])
    return f"""
            <h2>Students List</h2>
            <ul>{studentList}</ul>
        """
@app.route('/student/<int:x>')
def studend(x):
    student = students.get(x)
    if student:
        return f"""
            <h2>Details of Student {x}</h2>
            <p><b>Name:</b> {student['name']}</p>
            <p><b>Course:</b> {student['course']}</p>
        """
    else:
        return f"<h3>No student found with Roll No {x}</h3>"  
@app.route('/student/<int:x>/marks')
def studentt(x):
    student = students.get(x)
    if student:
        marks = student['marks']
        marks_list = "".join([f"<li>{subject}: {score}</li>" for subject, score in marks.items()])
        return f"""
            <h2>Marks of {student['name']} Roll No: {x}</h2>
            <ul>{marks_list}</ul>
        """
    else:
        return f"<h3>No marks found for Roll No {x}</h3>"
if __name__ == '__main__':
  app.run(debug=True)