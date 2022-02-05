import flask as fl
from sqlalchemy import extract, func
from flask import jsonify
from app import db
from models.app_models import Receitas
from serializer import receitas_schema, receita_schema
from flask_login import login_required

main_receitas = fl.Blueprint('main_receitas', __name__)

@main_receitas.route('/receitas', methods=['POST', 'GET'])
@login_required
def add_get_receitas():
    if fl.request.method == 'POST':
        descricao = fl.request.json['descricao']
        valor = fl.request.json['valor']
        data = fl.request.json['data']

        checking_duplicates = Receitas.query.filter(extract('year', 
            Receitas.data)==extract('year', data)).filter(extract('month', 
            Receitas.data)==extract('month', data)).filter(Receitas.descricao==descricao).one_or_none()
        if checking_duplicates is not None:
            return 'Esta receita já existe neste mês.'

        else:
            new_receita = {'descricao': descricao, 'valor': valor, 'data': data}
            db.session.execute(db.insert(Receitas),[new_receita])
            db.session.commit()
            return receita_schema.jsonify(new_receita)
    
    elif fl.request.method == 'GET':
        # adicionando busca ?descricao=descricao
        args = fl.request.args
        descricao = args.get('descricao')
        if descricao == None:
            all_receitas = db.session.query(Receitas).all()
            result = receitas_schema.dump(all_receitas)
            return jsonify(result)
        else:
            query=Receitas.query.filter(Receitas.descricao==descricao)
            result = receitas_schema.dump(query)
            return jsonify(result)

@main_receitas.route('/receitas/<id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def get_update_delete_receita(id):
    if fl.request.method == 'GET':
        receita = db.session.query(Receitas).get(id)
        return receita_schema.jsonify(receita)

    elif fl.request.method == 'PUT':
        receita = db.session.query(Receitas).get(id)
        descricao = fl.request.json['descricao']
        valor = fl.request.json['valor']
        data = fl.request.json['data']
        categoria = fl.request.json['categoria']

        checking_duplicates = Receitas.query.filter(extract('year', Receitas.data)==extract('year', data)).filter(
            extract('month', Receitas.data)==extract('month', data)).filter(Receitas.descricao==descricao).one_or_none()
        if checking_duplicates is not None:
            return 'Esta receita já existe neste mês.'

        else:
            receita.descricao = descricao
            receita.valor = valor
            receita.data = data
            receita.categoria = categoria

            db.session.commit()
            return receita_schema.jsonify(receita)

    elif fl.request.method == 'DELETE':
        receita = db.session.query(Receitas).get(id)
        db.session.delete(receita)
        db.session.commit()
        return receita_schema.jsonify(receita)

@main_receitas.route('/receitas/<int:ano>/<int:mes>', methods=['GET'])
@login_required
def get_receitas_ano_mes(ano,mes):
    if fl.request.method == 'GET':
        receitas = db.session.query(Receitas).filter(extract('year', Receitas.data)==ano).filter(extract('month', Receitas.data)==mes).all()
        result = receitas_schema.dump(receitas)
        return jsonify(result)