from app.extensions import ma
from .models import Funcionarios

class FuncionariosSchema(ma.SQLAlchemySchema):
    
    class Meta():
        model = Funcionarios
        load_instance = True
        ordered = True
        
    id = ma.Integer(dump_only=True)
    username = ma.String(required = True)