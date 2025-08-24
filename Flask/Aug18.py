# 5. Exam Grade + Attempt Check
# Route: /exam_result/<int:marks>/<int:attempt>
# • If marks ≥ 50 and attempt = 1 → "Pass (First Attempt)"
# • If marks ≥ 50 and attempt > 1 → "Pass (Repeat)"
# • Else → "Fail"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/exam_result/<int:marks>/<int:attempt>')
def home(marks, attempt):
    return render_template('Aug18.html', m=marks, a=attempt)

if __name__ == '__main__':
    app.run(debug=True)