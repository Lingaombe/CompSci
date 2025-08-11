from flask import Flask

app=Flask(__name__)

x=535

@app.route('/')
def home():
	return "Welcome to mathematics"

@app.route('/even_odd')
def even_odd():
	if x%2==0:
		return "535 is even number"
		
	else:
		return "535 is odd number"

@app.route('/pos_neg')
def pos_neg():
	if x<0:
		return "535 is negative"
		
	elif x>0:
		return "535 is positive"
		
	else:
		return "535 is zero"
		
@app.route('/fact')
def fact():
	i=1
	f=1
	while i<x:
		f=f*i
		i=i+1
	return "factorial is: " + str(f)
	
@app.route('/prime')
def prime():
	i=1
	c=0
	
	while i<=x:
		if x%i==0:
			c+=1
		i+=1
		
	if c<3:
		return "535 is prime"
		
	else:
		return "535 is not prime"
		
@app.route('/armstrong')
def armstrong():
	i=5**3
	j=3**3
	k=5**3
	s=i+j+k
	
	if s==x:
		return "535 is armstrong"
		
	else:
		return "535 is not armstrong"




