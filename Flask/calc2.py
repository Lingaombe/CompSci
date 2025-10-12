from flask import *
app = Flask(__name__)
@app.route('/calc/add/<int:x>/<int:y>')
def add(x,y):
  return f'<p>Sum of {x} and {y} is {x+y}</p>'
@app.route('/calc/sub/<int:x>/<int:y>')
def sub(x,y):
  return f'<p>Difference between {x} and {y} is {x-y}</p>'
@app.route('/calc/mul/<int:x>/<int:y>')
def mul(x,y):
  return f'<p>Product of {x} and {y} is {x*y}</p>'
@app.route('/calc/div/<int:x>/<int:y>')
def div(x,y):
  if y == 0:
    return f"<p>Can't divide by 0"
  return f'<p>Quotient of {x} and {y} is {x/y}</p>'
if __name__ == '__main__':
  app.run(debug=True)