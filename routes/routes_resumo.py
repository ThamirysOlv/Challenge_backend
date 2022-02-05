import flask as fl
from sqlalchemy import extract, func
from models.app_models import Receitas, Despesas
from flask_login import login_required


main_resumo = fl.Blueprint('main_resumo', __name__)

@main_resumo.route('/resumo/<int:ano>/<int:mes>', methods=['GET'])
@login_required
def get_resumo(ano,mes):
    if fl.request.method == 'GET':
        soma_despesas = Despesas.query.with_entities(func.sum(Despesas.valor).label('a')).filter(
            extract('year', Despesas.data)==ano).filter(extract('month', Despesas.data)==mes).first().a
        soma_receitas = Receitas.query.with_entities(func.sum(Receitas.valor).label('a')).filter(
            extract('year', Receitas.data)==ano).filter(extract('month', Receitas.data)==mes).first().a
        soma_despesas_por_categoria= Despesas.query.with_entities(Despesas.categoria, 
            func.sum(Despesas.valor).label('Total')).group_by(Despesas.categoria).filter(
            extract('year', Despesas.data)==ano).filter(extract('month', Despesas.data)==mes)

        resultset = [r._asdict() for r in soma_despesas_por_categoria]

        if soma_despesas == None:
            soma_despesas = 0
        if soma_receitas == None:
            soma_receitas = 0
            
        resumo={"Receitas": f"R$ {soma_receitas}",
                "Despesas": f"R$ {soma_despesas}",
                "Saldo": f"R$ {soma_receitas - soma_despesas}",
                "Despesas por categoria": resultset}
        return resumo