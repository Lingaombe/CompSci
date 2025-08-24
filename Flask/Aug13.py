# 1. Student Result Classification
# Route: /student_result/<int:marks>/<string:subject>
# • If marks < 35 → "Fail in <subject>"
# • If 35–50 → "Pass in <subject>"
# • If 51–75 → "First Class in <subject>"
# • Else → "Distinction in <subject>".

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student_result/<int:marks>/<subject>')
def home(marks, subject):
    return render_template('Aug13.html', m=marks, s=subject)

if __name__ == '__main__':
    app.run(debug=True)