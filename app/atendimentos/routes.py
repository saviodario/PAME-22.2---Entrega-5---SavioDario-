from flask import Blueprint
from .controller import AtendimentosClienteController,AtendimentosFuncionarioDetails,AtendimentosFuncionarioController,AtendimentosClienteDetails

atendimento_api = Blueprint("atendimento_api",__name__)

atendimento_api.add_url_rule(
    "/funcionarios/<int:funcionario_id>/atendimentos",
    view_func= AtendimentosFuncionarioController.as_view("atendimentos_funcionariocontroller"),
    methods = ["GET","POST"]
)

atendimento_api.add_url_rule(
    "/funcionarios/<int:funcionario_id>/atendimentos/<int:atendimento_id>",
    view_func= AtendimentosFuncionarioDetails.as_view("atendimentos_funcionariodetails"),
    methods = ["GET","PUT","DELETE"]
)

atendimento_api.add_url_rule(
    "/clientes/<int:cliente_id>/atendimentos",
    view_func= AtendimentosClienteController.as_view("atendimentos_clientecontroller"),
    methods = ["GET","POST"]
)

atendimento_api.add_url_rule(
    "/clientes/<int:cliente_id>/atendimentos/<int:atendimento_id>",
    view_func= AtendimentosClienteDetails.as_view("atendimentos_clientedetails"),
    methods = ["GET"]
)