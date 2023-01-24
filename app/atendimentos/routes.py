from flask import Blueprint
from .controller import AtendimentosDetails, AtendimentosController

atendimento_api = Blueprint("atendimento_api",__name__)

atendimento_api.add_url_rule(
    "/funcionarios/id/atendimentos",
    view_func= AtendimentosController.as_view("atendimentos_controller"),
    methods = ["GET","POST"]
)

atendimento_api.add_url_rule(
    "/funcionarios/<int:id>/Atendimentos/id",
    view_func= AtendimentosDetails.as_view("atendimentos_details"),
    methods = ["GET","PUT","PATCH","DELETE"]
)
