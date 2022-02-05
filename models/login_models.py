from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    nome = db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    

    def __init__(self, email, nome, senha):
        self.nome = nome
        self.senha = senha
        self.email = email