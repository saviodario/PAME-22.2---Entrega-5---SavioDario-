from app.models import BaseModel
from app.extensions import db
import bcrypt

class Clientes(BaseModel):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.LargeBinary(120))
    
    atendimentos = db.relationship("Atendimentos", backref="clientes")
    
    @property
    def password(self):
        raise AttributeError('password: write only field')
    
    @password.setter
    def password(self, senha) -> None:
        self.password_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        
    def check_password(self,senha) -> bool:
        return bcrypt.checkpw(senha.encode(),self.password_hash)