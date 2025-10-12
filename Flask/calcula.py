from flask import *
app = Flask(__name__)
@app.route('/calc/<int:x>/<int:y>/<op>')
def calc(x,y,op):
  if op == "add":
    res = x+y
  elif op == "sub":
    res = x-y
  elif op == "mul":
    res = x*y
  elif op == "div":
    res = x/y
  else:
    return f'<p>Choose operation add, sub, mul or div</p>'
  return f'<p>{res}</p>'
if __name__ == '__main__':
  app.run(debug=True)