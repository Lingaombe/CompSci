from flask import *
app = Flask(__name__)
@app.route('/string/reverse/<word>')
def rev(word):
  return f'<p>String {word} reversed is {word[::-1]}</p>'
@app.route('/string/uppercase/<word>')
def uppercase(word):
  return f'<p>String {word} uppercase is {word.upper()}</p>'
@app.route('/string/palindrome/<word>')
def palindrome(word):
  return f'<p>String {word} is palindrome {word.lower() == word.lower()[::-1]}</p>'
@app.route('/string/length/<word>')
def length(word):
  return f'<p>String {word} is length {len(word)}</p>'
if __name__ == '__main__':
  app.run(debug=True)