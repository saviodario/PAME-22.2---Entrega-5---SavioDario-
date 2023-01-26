from flask import Blueprint
from .controller import ClientesController,ClientesDetails,ClienteLogin

cliente_api = Blueprint("cliente_api",__name__)

cliente_api.add_url_rule(
    "/clientes",
    view_func= ClientesController.as_view("clientes_controller"),
    methods = ["POST"]
)

cliente_api.add_url_rule(
    "/clientes/<int:cliente_id>",
    view_func= ClientesDetails.as_view("clientes_details"),
    methods = ["GET","PUT","DELETE"]
)

cliente_api.add_url_rule(
    "/clientes/login",
    view_func= ClienteLogin.as_view("clientes_login"),
    methods = ["POST"]
)