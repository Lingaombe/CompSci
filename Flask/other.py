from flask import *
app = Flask(__name__)
@app.route('/result/<int:rno>/<name>/<int:m1>')
def result(x,y):
    return f"Sum = {(x+y)}"
if __name__ == '__main__':
  app.run(debug=True)