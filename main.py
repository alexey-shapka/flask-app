import logging
import os

import flask
import flask_login
from flask import Flask, render_template, redirect, request, Response
from flask_bcrypt import Bcrypt
from flask_login import login_required
from flask_restful import Api

from models import User
from utils import setup_logging, Config, database


path = os.path.dirname(os.path.abspath(__file__))

# init logger
logging_config_path = os.path.join(path, 'config', 'logging.yaml')
setup_logging(logging_config_path)
logger = logging.getLogger(__name__)

# load config
config_path = os.path.join(path, 'config', 'config.json')
config = Config(config_path)

# init Flask App
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = config['app']['secret_key']
app.config['PATH'] = path

with app.app_context():
    app.configuration = config

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{user}:{password}@{host}/{database}".format(
    **config['database']['sqlalchemy_database_uri'])
app.config['SQLALCHEMY_POOL_SIZE'] = config['database']['pool_size']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
database.init_app(app)

# init Flask login module with bcrypt hash
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)


@login_manager.user_loader
def user_loader(user_id):
    user = User.query.get(int(user_id))
    if not user:
        return

    return user


@login_manager.request_loader
def request_loader(login_request):
    login = login_request.form.get('login')
    user = User.query.filter_by(login=login).first()
    if not user:
        return

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    if 'api' in request.url:
        return Response(status=401)

    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    login = request.form.get('login')
    password = request.form.get('password')
    user = User.query.filter_by(login=login).first()
    if user and bcrypt.check_password_hash(user.password, password):
        flask_login.login_user(user)
        return flask.redirect('/listen')

    return render_template('login.html', error_message="Incorrect input data.")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    login = request.form.get('login')
    password = request.form.get('password')
    email = request.form.get('email')

    user = User(login, bcrypt.generate_password_hash(password), email)
    result = user.register()
    if result['status']:
        flask_login.login_user(user)
        return flask.redirect('/listen')

    return render_template('register.html', error_message=result['message'])


@app.route('/logout')
@login_required
def logout():
    flask_login.logout_user()
    return redirect('/login')


@app.route('/', methods=['GET'])
@login_required
def root():
    return redirect('/listen')


@app.route('/listen', methods=['GET'])
@login_required
def listen():
    return render_template('listen.html')


# api.add_resource(SearchResource, '/api/search')

if __name__ == '__main__':
    app.run(debug=True)
