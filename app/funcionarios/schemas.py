from app.extensions import ma
from .models import Funcionarios
from app.atendimentos.schemas import AtendimentosSchema
class FuncionariosSchema(ma.SQLAlchemySchema):
    
    class Meta():
        model = Funcionarios
        load_instance = True
        ordered = True
        
    id = ma.Integer(dump_only=True)
    username = ma.String(required = True)
    password = ma.String(load_only = True, required = True)
    
    atendimentos = ma.List(ma.Nested(AtendimentosSchema),dump_only = True)
    
class LoginFuncionarioSchema(ma.Schema):
    username = ma.String(required = True)
    password = ma.String(load_only = True, required = True)