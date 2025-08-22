from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hotelPrice/<room>/<int:days>/<season>/<day>')
def home(room,days,season,day):
	return render_template("Aug12.html", r=room, nod=days, s=season, tsiku=day)
	
if __name__ == '__main__':
	app.run(debug=True)
