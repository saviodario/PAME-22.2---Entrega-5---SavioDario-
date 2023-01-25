from app.models import BaseModel
from app.extensions import db

class Clientes(BaseModel):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    
    atendimentos = db.relationship("Atendimentos", backref="clientes")