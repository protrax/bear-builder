import json
from flask import (Flask, render_template, redirect,
				   url_for, request, make_response, 
				   flash)
from options import DEFAULTS

app = Flask(__name__)

app.secret_key = 'onsdfr>AU.oi.sh3$asd9098>$@*s54TY7@'


def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data


@app.route('/')
def index():
	return render_template('index.html', saves=get_saved_data())


@app.route('/save', methods=['POST'])
def save():
	flash('Alright that looks awesome!', )
	response = make_response(redirect(url_for('builder')))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response


@app.route('/builder')
def builder():
	return render_template(
		'builder.html',
		saves=get_saved_data(),
		options=DEFAULTS
	)

if __name__ == "__main__":
	app.run(debug=True, port=8000, host='0.0.0.0')
