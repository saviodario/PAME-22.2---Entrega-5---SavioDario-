from app.models import BaseModel
from app.extensions import db

class Insumos(BaseModel):
    __tablename__ = "insumos"
    
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(30))
    quantidade = db.Column(db.Integer)
    
    atendimento_id = db.Column(db.Integer, db.ForeignKey("atendimentos.id"))