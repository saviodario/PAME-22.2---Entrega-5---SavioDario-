from flask import Blueprint
from .controller import FuncionariosController,FuncionariosDetails

funcionario_api = Blueprint("funcionario_api",__name__)

funcionario_api.add_url_rule(
    "/funcionarios",
    view_func= FuncionariosController.as_view("funcionarios_controller"),
    methods = ["GET","POST"]
)

funcionario_api.add_url_rule(
    "/funcionarios/<int:id>",
    view_func= FuncionariosDetails.as_view("funcionarios_details"),
    methods = ["GET","PUT","DELETE"]
)
