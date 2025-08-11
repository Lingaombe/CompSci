from flask import Flask
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<int:z>')
def home(x,y,z):
    return "Sum is: "+str(x+y+z)+"<br>Average is: "+str((x+y+z)/3)