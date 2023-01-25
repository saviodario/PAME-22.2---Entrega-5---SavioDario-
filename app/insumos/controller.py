from flask import request
from flask.views import MethodView

from .schemas import InsumosSchema
from .models import Insumos
from app.atendimentos.models import Atendimentos

class InsumosAtendimentoController(MethodView):
    def get(self,atendimento_id):
        schema = InsumosSchema()
        atendimento = Atendimentos.query.get(atendimento_id)
        if not atendimento:
            return{},404
        insumos = insumos.query.filter_by(atendimento_id=atendimento_id)
        return schema.dump(insumos, many = True), 200
    
    def post(self,atendimento_id):
        schema = InsumosSchema()
        atendimento = Atendimentos.query.get(atendimento_id)
        if not atendimento:
            return{},404
        data = request.json
        data['atendimento_id'] = atendimento_id
        try:
            post = schema.load(data)
        except:
            return {},400
        post.save()
        return schema.dump(post), 201
    
class InsumosAtendimentoDetails(MethodView):
    def get(self,atendimento_id,insumos_id):
        schema = InsumosSchema()
        insumo = Insumos.query.get(insumos_id)
        if not insumo:
            return {'error: resourse not found'},404
        return schema.dump(insumo)
        
    def put(self,atendimento_id,insumos_id):
        schema = InsumosSchema()
        
        data = request.json
        insumo = Insumos.query.get(insumos_id)
        if not insumo:
            return {'error: resourse not found'},404
        try:
            insumo = schema.load(data, instance=insumo)
        except:
            return{},400
        insumo.save()
        return schema.dump(insumo),201
    
    def delete(self,atendimento_id,insumos_id):
        schema = InsumosSchema()
        insumo = Insumos.query.get(insumos_id)
        if not insumo:
            return {'error: resourse not found'},404
        
        insumo.delete(insumo)
        return {},204
            
