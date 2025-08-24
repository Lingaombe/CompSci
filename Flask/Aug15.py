# 3. Movie Ticket Pricing
# Route: /ticket_price/<int:age>/<string:day>
# • If age < 12 → Child discount 50%
# • If age ≥ 60 → Senior discount 30%
# • If day = "wednesday" → Extra 10% off.
# • Return calculated ticket price.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ticket_price/<int:age>/<day>')
def home(age, day):
    return render_template('Aug15.html', d=day, a=age)

if __name__ == '__main__':
    app.run(debug=True)