from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
	return "<h1>Vivekanand College, Kolhapur</h1><br><h2>An empowered autonomous institute</h2><br><p>Established in 1964</p>"

	

