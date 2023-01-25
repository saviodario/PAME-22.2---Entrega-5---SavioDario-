from flask import request
from flask.views import MethodView

from .schemas import ClientesSchema
from .models import Clientes

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
    def get(self,cliente_id):
        schema = ClientesSchema()
        cliente = Clientes.query.get(cliente_id)
        if not cliente:
            return {'error: user not found'},404
        return schema.dump(cliente)
        
    
    def put(self,cliente_id):
        schema = ClientesSchema()
        
        data = request.json
        cliente = Clientes.query.get(cliente_id)
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
        if not cliente:
            return {'error: user not found'},404
        
        cliente.delete(cliente)
        return {},204
            
            
