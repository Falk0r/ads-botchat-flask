from flask import Flask, render_template
from controllers.ads import getAllAds

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/ads')
def ads():
	ads = getAllAds()
	return render_template('users.html', ads=ads)

@app.route('/login')
def login():
	return render_template('login.html')