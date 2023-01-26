from app.models import BaseModel
from app.extensions import db
import bcrypt

class Funcionarios(BaseModel):
    __tablename__ = "funcionarios"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.LargeBinary(120))
    
    atendimentos = db.relationship("Atendimentos", backref="funcionarios")
    
    @property
    def password(self):
        raise AttributeError('password: write only field')
    
    @password.setter
    def password(self, password) -> None:
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
    def check_password(self,password):
        return bcrypt.checkpw(password.encode(),self.password_hash)