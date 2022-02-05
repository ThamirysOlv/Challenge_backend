import flask as fl
from sqlalchemy import extract, func
from flask import jsonify
from app import db
from models.app_models import Despesas, categoria_options
from serializer import despesa_schema, despesas_schema
from flask_login import login_required

main_despesas = fl.Blueprint('main_despesas', __name__)

@main_despesas.route('/despesas', methods=['POST', 'GET'])
@login_required
def add_get_despesas():
    if fl.request.method == 'POST':
        try:
            descricao = fl.request.json['descricao']
            valor = fl.request.json['valor']
            data = fl.request.json['data']
            categoria = fl.request.json['categoria']

        except:
            descricao = fl.request.json['descricao']
            valor = fl.request.json['valor']
            data = fl.request.json['data']
            categoria = "Outras"
        finally:
            if categoria not in categoria_options:
                return f'Escolha uma categoria válida: {categoria_options}'
            else:
                checking_duplicates = Despesas.query.filter(extract('year', 
                    Despesas.data)==extract('year', data)).filter(extract('month', 
                    Despesas.data)==extract('month', data)).filter(Despesas.descricao==descricao).one_or_none()
                if checking_duplicates is not None:
                    return 'Esta despesa já existe neste mês.'

                else:
                    new_despesa = {'descricao': descricao, 'valor': valor, 'data': data, 'categoria': categoria}
                    db.session.execute(db.insert(Despesas),[new_despesa])
                    db.session.commit()
                    return despesa_schema.jsonify(new_despesa)
    
    elif fl.request.method == 'GET':
        # adicionando busca ?descricao=descricao
        args = fl.request.args
        descricao = args.get('descricao')
        if descricao == None:
            all_despesas = db.session.query(Despesas).all()
            result = despesas_schema.dump(all_despesas)
            return jsonify(result)
        else:
            query=Despesas.query.filter(Despesas.descricao==descricao)
            result = despesas_schema.dump(query)
            return jsonify(result)

@main_despesas.route('/despesas/<id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def get_update_delete_despesa(id):
    if fl.request.method == 'GET':
        despesa = db.session.query(Despesas).get(id)
        return despesa_schema.jsonify(despesa)

    elif fl.request.method == 'PUT':
        despesa = db.session.query(Despesas).get(id)
        descricao = fl.request.json['descricao']
        valor = fl.request.json['valor']
        data = fl.request.json['data']

        checking_duplicates = Despesas.query.filter(extract('month', Despesas.data)==extract('month', data)).filter(Despesas.descricao==descricao).one_or_none()
        if checking_duplicates is not None:
            return 'Esta despesa já existe neste mês.'

        else:
            despesa.descricao = descricao
            despesa.valor = valor
            despesa.data = data

            db.session.commit()
            return despesa_schema.jsonify(despesa)

    elif fl.request.method == 'DELETE':
        despesa = db.session.query(Despesas).get(id)
        db.session.delete(despesa)
        db.session.commit()
        return despesa_schema.jsonify(despesa)

@main_despesas.route('/despesas/<int:ano>/<int:mes>', methods=['GET'])
@login_required
def get_despesas_ano_mes(ano,mes):
    if fl.request.method == 'GET':
        despesas = db.session.query(Despesas).filter(extract('year', Despesas.data)==ano).filter(extract('month', Despesas.data)==mes).all()
        result = despesas_schema.dump(despesas)
        return jsonify(result)