from app.extensions import ma
from .models import Insumos
class InsumosSchema(ma.SQLAlchemySchema):
    
    class Meta():
        model = Insumos
        load_instance = True
        ordered = True
        
    id = ma.Integer(dump_only=True)
    tipo = ma.String(required = True)
    quantidade = ma.Integer(required = True)
    
    atendimento_id = ma.Integer()
    
