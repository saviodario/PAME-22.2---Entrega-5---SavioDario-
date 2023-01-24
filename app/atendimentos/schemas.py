from app.extensions import ma
from .models import Atendimentos

class AtendimentosSchema(ma.SQLAlchemySchema):
    
    class Meta():
        model = Atendimentos
        load_instance = True
        ordered = True
        
    id = ma.Integer(dump_only=True)
    data = ma.String()
    hora = ma.String()
    etapa = ma.String()
    funcionario_id = ma.Integer()