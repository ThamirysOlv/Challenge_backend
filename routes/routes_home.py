import flask as fl
from app import db
from flask_login import login_required, current_user

home_route = fl.Blueprint('home_route', __name__)

@home_route.route('/', methods=['GET'])
def home():
    render_html = """<h1>Olá!</h1>
    <h2>Faça login em /login ou signup em /signup</h2>
    <h2>Para login entre email e senha </h2>
    <h2>Para signup entre email, nome, e senha </h2>
    """
    return render_html

@home_route.route('/profile', methods=['GET'])
@login_required
def profile():
    render_html = """<h1>Olá!</h1>
    <h2> Para acessar ou cadastrar despesas: /despesas </h2>
    <h2> Para acessar ou cadastrar receitas: /receitas </h2>
    <h2> Para acessar, alterar, ou deletar uma despesa: /despesas/{id} </h2>
    <h2> Para acessar, alterar, ou deletar uma receita: /receitas/{id} </h2>
    <h2> Para buscar uma despesa pela descrição: /despesas?descricao={descricao} </h2>
    <h2> Para buscar uma receita pela descrição: /receitas?descricao={descricao} </h2>
    <h2> Para buscar despesas de um determinado mês: /receitas/{ano}/{mes} </h2>
    <h2> Para buscar receitas de um determinado mês: /receitas/{ano}/{mes} </h2>

    <h2> Para buscar o resumo de um determinado mês: /resumo/{ano}/{mes} </h2>

    <h2> Para logout: /logout </h2>

    """
    return render_html