from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
from models.ads import getAllAds
from models.users import getAllUsers, findUser, addUser
from controllers.auth import toLog

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

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

@app.route('/old-register', methods=['GET', 'POST'])
def old_register():
	if request.method == 'POST':
		# print(request.form['email'], request.form['password'], request.form['name'])
		print(request.get_json())
		if (request.form['email'] and request.form['password'] and request.form['name']):
			check = findUser(request.form['email'])
			if (not check):
				print("add an user")
				addUser(request.form['name'], request.form['email'], request.form['password'])
		else:
			return jsonify('error !')

		# Incorrect values
		# return redirect('/login', code=302, Response=None)
		return jsonify('error !')
	else:
		# Get route
		print('redirection vers login')
		return redirect('/login', code=302, Response=None)

@app.route('/old-login', methods=['GET', 'POST'])
def old_login():
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

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		user = request.get_json()
		print(user['name'])
		if (user['name'] and user['email'] and user['password']):
			check = findUser(user['email'])
			if (not check):
				newUser = addUser(user['name'], user['email'], user['password'])
				print (newUser)
				return jsonify(newUser)
			else:
				return jsonify('User Already exist')
		else:
			return jsonify('Data invalid')
	else:
		return jsonify('GET METHOD !')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.get_json()
		if (user['email'] and user['password']):
			token = toLog(user)
			if (token):
				return jsonify({'Token': token, 'authenticated': True})
			else:
				return jsonify({'Message': 'Invalid credentials', 'authenticated': False}), 401
		else:
			return jsonify({'Message': 'Data invalid', 'authenticated': False}), 401
	else:
		return jsonify('GET METHOD !')

if __name__ == '__main__':
	app.run()