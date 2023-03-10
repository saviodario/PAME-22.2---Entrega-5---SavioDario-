from app.extensions import ma
from .models import Clientes
from app.atendimentos.schemas import AtendimentosSchema
class ClientesSchema(ma.SQLAlchemySchema):
    
    class Meta():
        model = Clientes
        load_instance = True
        ordered = True
        
    id = ma.Integer(dump_only=True)
    username = ma.String(required = True)
    password = ma.String(load_only = True, required = True)
    
    atendimentos = ma.List(ma.Nested(AtendimentosSchema),dump_only = True)
    
class LoginClienteSchema(ma.Schema):
    username = ma.String(required = True)
    password = ma.String(load_only = True, required = True)