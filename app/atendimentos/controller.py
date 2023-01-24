from flask import request
from flask.views import MethodView

from .schemas import AtendimentosSchema
from .models import Atendimentos
from app.funcionarios.models import Funcionarios

class AtendimentosController(MethodView):
    def get(self,funcionario_id):
        schema = AtendimentosSchema()
        atendimentos = Atendimentos.query.all()

        return schema.dump(atendimentos, many = True), 200
    
    def post(self,funcionario_id):
        pass
    
class AtendimentosDetails(MethodView):    
    def put(self,funcionario_id,atendimento_id):
        pass
    
    def patch(self,funcionario_id,atendimento_id):
        pass
    
    def delete(self,funcionario_id,atendimento_id):
        pass
            
