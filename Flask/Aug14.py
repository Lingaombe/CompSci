# 2. E-commerce Free Shipping
# Route: /order/<int:amount>/<string:member>
# • If member = "prime" → "Free shipping" regardless of amount.
# • Else if amount ≥ 1000 → "Free shipping"
# • Else → "Shipping charges apply"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/order/<int:amount>/<member>')
def home(amount, member):
    return render_template('Aug14.html', m=member, a=amount)

if __name__ == '__main__':
    app.run(debug=True)