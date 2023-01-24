from flask import request
from flask.views import MethodView

from .schemas import FuncionariosSchema
from .models import Funcionarios

class FuncionariosController(MethodView):
    def get(self):
        schema = FuncionariosSchema()
        funcionarios = Funcionarios.query.all()

        return schema.dump(funcionarios, many = True), 200
    
    def post(self):
        schema = FuncionariosSchema()
        data = request.json
        try:
            funcionario = schema.load(data)
        except:
            return{},400
        funcionario.save()
        return schema.dump(funcionario),201
    
class FuncionariosDetails(MethodView):
    def get(self,id):
        schema = FuncionariosSchema()
        funcionario = Funcionarios.query.get(id)
        if not funcionario:
            return {'error: user not found'},404
        return schema.dump(funcionario)
        
    
    def put(self,id):
        schema = FuncionariosSchema()
        
        data = request.json
        funcionario = Funcionarios.query.get(id)
        if not funcionario:
            return {'error: user not found'},404
        try:
            funcionario = schema.load(data, instance=funcionario)
        except:
            return{},400
        funcionario.save()
        return schema.dump(funcionario),201
    
    def delete(self,id):
        schema = FuncionariosSchema()
        funcionario = Funcionarios.query.get(id)
        if not funcionario:
            return {'error: user not found'},404
        
        funcionario.delete(funcionario)
        return {},204
            
