import flask as fl
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager



# initialize db, migrate e ma
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = fl.Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/challenge'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "secret_key"

    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)

    # blueprint for auth routes in our app
    from routes.routes_login import auth
    app.register_blueprint(auth)

    # blueprint for non-auth parts of app
    # order maters! importe rotas aqui e nao no topo do documento
    from routes.routes_receitas import main_receitas
    from routes.routes_despesas import main_despesas
    from routes.routes_resumo import main_resumo
    from routes.routes_home import home_route
    app.register_blueprint(main_receitas)
    app.register_blueprint(main_despesas)
    app.register_blueprint(main_resumo)
    app.register_blueprint(home_route)


    lm = LoginManager()
    lm.login_view = "auth.login"
    lm.init_app(app)
    
    from models.login_models import User
    @lm.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    # debug=True shows on the page any errors that may occur
    create_app().run(debug=True)