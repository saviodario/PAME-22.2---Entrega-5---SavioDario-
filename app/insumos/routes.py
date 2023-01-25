from flask import Blueprint
from .controller import InsumosAtendimentoController,InsumosAtendimentoDetails

insumo_api = Blueprint("insumo_api",__name__)

insumo_api.add_url_rule(
    "/atendimentos/<int:atendimento_id>/insumos",
    view_func= InsumosAtendimentoController.as_view("insumos_controller"),
    methods = ["GET","POST"]
)

insumo_api.add_url_rule(
    "/atendimentos/<int:atendimento_id>/insumos/<int:insumos_id>",
    view_func= InsumosAtendimentoDetails.as_view("insumos_details"),
    methods = ["GET","PUT","DELETE"]
)
