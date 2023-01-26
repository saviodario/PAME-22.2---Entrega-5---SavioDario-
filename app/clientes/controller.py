from flask import request
from flask.views import MethodView

from .schemas import ClientesSchema,LoginClienteSchema
from .models import Clientes
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity


"/clientes"
class ClientesController(MethodView):    
    "possibilita cliente criar conta"
    def post(self):
        schema = ClientesSchema()
        data = request.json
        try:
            cliente = schema.load(data)
        except:
            return{},400
        cliente.save()
        return schema.dump(cliente),201

"/clientes/<int:cliente_id>"
class ClientesDetails(MethodView):
    "gerenciamento da conta pessoal do cliente alteração de nome e remoção do sistema "
    
    decorators = [jwt_required()]
    
    def get(self,cliente_id):
        schema = ClientesSchema()
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return {'error: user not found'},404
        return schema.dump(cliente)
        
    
    def put(self,cliente_id):
        schema = ClientesSchema()
        
        data = request.json
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return {'error: user not found'},404
        try:
            cliente = schema.load(data, instance=cliente)
        except:
            return{},400
        cliente.save()
        return schema.dump(cliente),201
    
    def delete(self,cliente_id):
        schema = ClientesSchema()
        cliente = Clientes.query.get(cliente_id)
        if cliente_id!=get_jwt_identity():
            return{"error":"crendentials invalid"},401
        if not cliente:
            return {'error: user not found'},404
        
        cliente.delete(cliente)
        return {},204
            
class ClienteLogin(MethodView):
    def post(self):
        schema = LoginClienteSchema()
        data = schema.load(request.json)
        
        cliente = Clientes.query.filter_by(username=data['username']).first()
        
        if not cliente:
            return {'error: user not found'},404
        
        if not cliente.check_password(data['password']):
            return {"error":"wrong password"},401
        
        token = create_access_token(identity = cliente.id)
        
        return {"funcionario": ClientesSchema().dump(cliente),"token":token},200
