from flask import *
app = Flask(__name__)
@app.route('/result/<int:x>/<name>/<int:m1>/<int:m2>/<int:m3>')
def result(x,name,m1,m2,m3):
  p = (m1+m2+m3)/3
  if p < 40:
    g = "Fail"
  elif p < 50:
    g = "Pass"
  elif p < 60:
    g = "second class"
  elif p > 70:
    g = "first class"
  else:
    g = "distinction"   
  return f"""<h1>Results of {name}</h1>
      <p>Roll number: {x}</p><p>Marks of subject 1: {m1}</p>
      <p>Marks of subject 2: {m2}</p><p>Marks of subject 3: {m3}</p>
      <p>Total Marks: {m1+m2+m3}</p><p>Percentage: {p}</p>
      <p>Your grade is: {g}</p>
  """  
if __name__ == '__main__':
  app.run(debug=True)