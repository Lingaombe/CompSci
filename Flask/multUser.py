from flask import *

app = Flask(__name__)

@app.route('/')
def result():
    students = [ 
    {"name": "Rajashree", "marks": 85}, 
    {"name": "Anita", "marks": 72}, 
    {"name": "Soham", "marks": 39} 
    ]  
    return render_template("multUser.html", stock=students)
  
if __name__ == '__main__':
  app.run(debug=True)