from flask import Flask

from .extensions import ma, db, mi, jwt
from .config import Config

from app.funcionarios.routes import funcionario_api
from app.clientes.routes import cliente_api
from app.atendimentos.routes import atendimento_api
from app.insumos.routes import insumo_api

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    ma.init_app(app)
    db.init_app(app)
    mi.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(funcionario_api)
    app.register_blueprint(cliente_api) 
    app.register_blueprint(atendimento_api)
    app.register_blueprint(insumo_api)
    
    return app