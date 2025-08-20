from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:x>')
def home(x):
    return render_template("Aug16.html", num=x)

if __name__ == '__main__':
    app.run(debug=True)