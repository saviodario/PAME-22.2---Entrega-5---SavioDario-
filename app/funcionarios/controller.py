from flask import request
from flask.views import MethodView

from .schemas import FuncionariosSchema, LoginFuncionarioSchema
from .models import Funcionarios
from flask_jwt_extended import create_access_token,jwt_required

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
    
    decorators = [jwt_required]
    
    def get(self,funcionarios_id):
        schema = FuncionariosSchema()
        funcionario = Funcionarios.query.get(funcionarios_id)
        if not funcionario:
            return {'error: user not found'},404
        return schema.dump(funcionario)
        
    
    def put(self,funcionarios_id):
        schema = FuncionariosSchema()
        
        data = request.json
        funcionario = Funcionarios.query.get(funcionarios_id)
        if not funcionario:
            return {'error: user not found'},404
        try:
            funcionario = schema.load(data, instance=funcionario)
        except:
            return{},400
        funcionario.save()
        return schema.dump(funcionario),201
    
    def delete(self,funcionarios_id):
        schema = FuncionariosSchema()
        funcionario = Funcionarios.query.get(funcionarios_id)
        if not funcionario:
            return {'error: user not found'},404
        
        funcionario.delete(funcionario)
        return {},204
    
class FuncionarioLogin(MethodView):
    def post(self):
        schema = LoginFuncionarioSchema()
        data = schema.load(request.json)
        
        funcionario = Funcionarios.query.filter_by(username=data['username']).first()
        
        if not funcionario:
            return {'error: user not found'},404
        
        if not funcionario.check_password(data['password']):
            return {"error":"wrong password"},401
        
        token = create_access_token(identity = funcionario.id)
        
        return schema.dump(funcionario),200
            
