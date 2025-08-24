# 4. Employee Bonus Eligibility
# Route: /bonus/<int:experience>/<string:performance>
# • If experience ≥ 5 and performance = "excellent" → Bonus 20%
# • If performance = "good" → Bonus 10%
# • Else → No bonus

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bonus/<int:exp>/<string:per>')
def home(exp, per):
    return render_template('Aug17.html', p=per, e=exp)

if __name__ == '__main__':
    app.run(debug=True)