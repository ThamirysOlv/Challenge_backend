from app import db
class Receitas(db.Model):
    __tablename__ = 'receitas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Numeric, nullable=False)
    data = db.Column(db.Date, nullable=False)
    

    def __init__(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = valor
        self.data = data

categoria_options = ['Alimentação', 'Saúde', 'Moradia', 'Transporte', 'Educação', 'Lazer', 'Imprevistos', 'Outras']
class Despesas(db.Model):
    __tablename__ = 'despesas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Numeric, nullable=False)
    data = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(200))

    def __init__(self, descricao, valor, data, categoria):
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria

