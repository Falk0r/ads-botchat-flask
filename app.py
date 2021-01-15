from flask import Flask, render_template, redirect, url_for, request
from models.ads import getAllAds
from models.users import getAllUsers, findUser, addUser
from controllers.auth import toLog

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/ads')
def ads():
	ads = getAllAds()
	return render_template('users.html', ads=ads)

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		print(request.form['email'], request.form['password'], request.form['name'])
		if (request.form['email'] and request.form['password'] and request.form['name']):
			check = findUser(request.form['email'])
			if (not check):
				print("add an user")
				addUser(request.form['name'], request.form['email'], request.form['password'])

		# Incorrect values
		return redirect('/login', code=302, Response=None)
	else:
		# Get route
		print('redirection vers login')
		return redirect('/login', code=302, Response=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if (request.form['email'] and request.form['password']):
			user = {
				"email" : request.form['email'],
				"password" : request.form['password']
			}
			isLog = toLog(user)
			if isLog:
				print(isLog)
				response = app.make_response(render_template('dashboard.html'))
				response.headers['x-access-token'] = isLog
				return response
			else:
				# Todo : Add error message
				pass
		pass
	else:
		pass
	users = getAllUsers()
	return render_template('login.html', users=users)

if __name__ == '__main__':
	app.run()