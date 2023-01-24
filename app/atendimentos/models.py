from app.models import BaseModel
from app.extensions import db

class Atendimentos(BaseModel):
    __tabelname__ = "atendimentos"
    
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(12))
    hora = db.Column(db.String(12))
    etapa = db.Column(db.String(20))
    username = db.Column(db.String(20))
    
    funcionario_id = db.Column(db.Integer, db.ForeignKey("funcionarios.id"))