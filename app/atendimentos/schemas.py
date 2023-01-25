from app.extensions import ma
from .models import Atendimentos
from app.insumos.schemas import InsumosSchema

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
    cliente_id = ma.Integer()
    insumos = ma.List(ma.Nested(InsumosSchema),dump_only = True)