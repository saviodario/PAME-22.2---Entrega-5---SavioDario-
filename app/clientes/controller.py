from flask import request
from flask.views import MethodView

from .schemas import ClientesSchema
from .models import Clientes

""" class ClientesController(MethodView):
    def get(self):
        schema = ClientesSchema()
        clientes = Clientes.query.all()

        return schema.dump(clientes, many = True), 200
    
    def post(self):
        schema = ClientesSchema()
        data = request.json
        try:
            cliente = schema.load(data)
        except:
            return{},400
        cliente.save()
        return schema.dump(cliente),201
    
class ClientesDetails(MethodView):
    def get(self,id):
        schema = ClientesSchema()
        cliente = Clientes.query.get(id)
        if not cliente:
            return {'error: user not found'},404
        return schema.dump(cliente)
        
    
    def put(self,id):
        schema = ClientesSchema()
        
        data = request.json
        cliente = Clientes.query.get(id)
        if not cliente:
            return {'error: user not found'},404
        try:
            cliente = schema.load(data, instance=cliente)
        except:
            return{},400
        cliente.save()
        return schema.dump(cliente),201
    
    def delete(self,id):
        schema = ClientesSchema()
        cliente = Clientes.query.get(id)
        if not cliente:
            return {'error: user not found'},404
        
        cliente.delete(cliente)
        return {},204
            
            
 """