from flask import request
from flask.views import MethodView

from .schemas import AtendimentosSchema
from .models import Atendimentos
from app.funcionarios.models import Funcionarios
from app.clientes.models import Clientes
from flask_jwt_extended import jwt_required,get_jwt_identity

"/funcionarios/<int:funcionario_id>/atendimentos"
class AtendimentosFuncionarioController(MethodView):
    
    decorators = [jwt_required()]
    
    def get(self,funcionario_id):
        schema = AtendimentosSchema()
        funcionario = Funcionarios.query.get(funcionario_id)
        if funcionario_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not funcionario:
            return{},404
        atendimentos = Atendimentos.query.filter_by(funcionario_id=funcionario_id)

        return schema.dump(atendimentos, many = True), 200
    
    def post(self,funcionario_id):
        schema = AtendimentosSchema()
        funcionario = Funcionarios.query.get(funcionario_id)
        if funcionario_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not funcionario:
            return{},404
        data = request.json
        data['funcionario_id'] = funcionario_id
        try:
            post = schema.load(data)
        except:
            return {},400
        post.save()
        return schema.dump(post), 201

"/funcionarios/<int:funcionario_id>/atendimentos/<int:atendimento_id>"
class AtendimentosFuncionarioDetails(MethodView):   
    "avanço de etapas e gerenciamentos dos atendimentos por parte do funcionário"
    
    decorators = [jwt_required()]
    
    def get(self,funcionario_id,atendimento_id):
        schema = AtendimentosSchema()
        funcionario = Funcionarios.query.get(funcionario_id)
        if funcionario_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not funcionario:
            return{},404
        atendimento = Atendimentos.query.get(atendimento_id)
        if not atendimento:
            return {'error: service not found'},404
        return schema.dump(atendimento)
     
    def put(self,funcionario_id,atendimento_id):
        schema = AtendimentosSchema()
        
        data = request.json
        if funcionario_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        funcionario = Funcionarios.query.get(funcionario_id)
        if not funcionario:
            return{},404
        
        atendimento =Atendimentos.query.get(atendimento_id)
        if not atendimento:
            return {'error: user not found'},404
        try:
            atendimento = schema.load(data, instance=atendimento)
        except:
            return{},400
        atendimento.save()
        return schema.dump(atendimento),201
    
    def delete(self,funcionario_id,atendimento_id):
        funcionario = Funcionarios.query.get(funcionario_id)
        if funcionario_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not funcionario:
            return{},400
        atendimento = Atendimentos.query.get(atendimento_id)
        if not atendimento:
            return{},400
        if atendimento not in funcionario.atendimentos:
            return {},401
        atendimento.delete(atendimento)
        return {},204
    
"/clientes/<int:cliente_id>/atendimentos"
class AtendimentosClienteController(MethodView):
    decorators = [jwt_required()]
    def get(self,cliente_id):
        schema = AtendimentosSchema()
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return{},404
        atendimentos = Atendimentos.query.filter_by(cliente_id=cliente_id)

        return schema.dump(atendimentos, many = True), 200
    
    "marcador de consultas"
    def post(self,cliente_id):
        schema = AtendimentosSchema()
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return{},404
        data = request.json
        data['cliente_id'] = cliente_id
        try:
            atendimento= schema.load(data)
        except:
            return {},400
        atendimento.save()
        return schema.dump(atendimento), 201
 
"/clientes/<int:cliente_id>/atendimentos/<int:atendimento_id>"           
class AtendimentosClienteDetails(MethodView):   
    decorators = [jwt_required()]
    def get(self,cliente_id,atendimento_id):
        schema = AtendimentosSchema()
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return{},404
        cliente = Clientes.query.get(cliente_id)
        if not cliente:
            return {'error: service not found'},404
        return schema.dump(cliente)
    
    
    