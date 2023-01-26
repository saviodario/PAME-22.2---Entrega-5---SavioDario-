from flask import Blueprint
from .controller import FuncionariosController,FuncionariosDetails,FuncionarioLogin

funcionario_api = Blueprint("funcionario_api",__name__)

funcionario_api.add_url_rule(
    "/funcionarios",
    view_func= FuncionariosController.as_view("funcionarios_controller"),
    methods = ["GET","POST"]
)

funcionario_api.add_url_rule(
    "/funcionarios/<int:funcionarios_id>",
    view_func= FuncionariosDetails.as_view("funcionarios_details"),
    methods = ["GET","PUT","DELETE"]
)

funcionario_api.add_url_rule(
    "/funcionarios/login",
    view_func= FuncionarioLogin.as_view("funcionarios_login"),
    methods = ["POST"]
)