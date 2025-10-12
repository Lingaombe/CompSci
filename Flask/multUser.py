from flask import *
app = Flask(__name__)
@app.route('/')
def result():
    stock = {"Shirt": 20, "Shoes": 0, "Hat": 15}  
    return render_template("multUser.html", stock=stock)
if __name__ == '__main__':
  app.run(debug=True)