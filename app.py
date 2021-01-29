from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
import jwt
from models.ads import getAllAds, addAd, deleteAd
from models.users import getAllUsers, findUser, addUser
from controllers.auth import toLog, decode_auth_token

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/ads')
def getads():
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

# Token Decorator for api routes
def token_required(f):
    # @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = decode_auth_token(token)
            user = findUser(email=data['userEmail'])
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

# API ROUTING
@app.route('/api/ads', methods=['GET', 'POST', 'DELETE'])
@token_required
def ads(current_user):
	if request.method == 'POST':
		ad = request.get_json()
		newAd = addAd(ad, current_user)
		if newAd:
			return jsonify({'message' : 'Ad created !'})
		else:
			return jsonify({'message' : 'Ad not created !'}), 500
	elif request.method == 'DELETE':
		ad = request.get_json()
		print(current_user)
		print(ad)
		removeAd = deleteAd(ad, current_user)
		if removeAd:
			return jsonify({'message' : 'Ad deleted !'})
		else:
			return jsonify({'message' : 'Ad not deleted !'}), 500

	else:
		id = str(current_user['_id'])
		ads = getAllAds(id)
		print(id)
		return jsonify(ads)



if __name__ == '__main__':
	app.run()