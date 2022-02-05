import flask as fl
from app import db
from models.login_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from serializer import user_schema, users_schema
from flask_login import login_user, logout_user

auth = fl.Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    email = fl.request.json['email']
    password = fl.request.json['senha']

    checking_email = User.query.filter(User.email==email).one_or_none()
    if checking_email is not None:
        get_senha = db.session.query(User.senha).filter(User.email==email).all()
        checking_senha = check_password_hash(get_senha[0][0], password)
    if checking_email is None or checking_senha is False:
        message = """<h2>E-mail e/ou senha incorretos.</h2>"""
        return message

    else:
        login_user(checking_email)
        return fl.redirect(fl.url_for('home_route.profile'))

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    email = fl.request.json['email']
    nome = fl.request.json['nome']
    password = fl.request.json['senha']

    checking_duplicates = User.query.filter(User.email==email).one_or_none()
    if checking_duplicates is not None:
        #message = """<h2>Usuario já cadastrado, vá para a <a href="{{ fl.url_for('auth.login') }}">página de login</a>.</h2>"""
        message = """<h2>Usuario já cadastrado, vá para a página de login.</h2>"""
        #return fl.redirect(fl.url_for('auth.login'))
        return message

    else:
        new_user = {'email': email, 'nome': nome, 'senha': generate_password_hash(password, method='sha256')}
        db.session.execute(db.insert(User),[new_user])
        db.session.commit()
        #fl.flash('Usuário cadastrado com sucesso, redirecionando para a página de login.')
        message = """<h2>Usuário cadastrado com sucesso, vá para a página de login.</h2>"""
        return message

@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return fl.redirect(fl.url_for('home_route.home'))