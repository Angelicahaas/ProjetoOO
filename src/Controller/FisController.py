from Model.pessoafisica import PessoaFisica
from Model.pessoajuridica import PessoaJuridica
from Model.gerente import Gerente
import json

class Controller:

    def __init__(self, usuario_lista, gerente_lista, DirListaC, DirListaG):
        self.cliente_lista = usuario_lista
        self.gerente_lista = gerente_lista
        self.DirListaC = DirListaC
        self.DirListaG = DirListaG


    def atualizar_json(self):

        with open(self.DirListaG, "w") as AtualizarArqG:
            json.dump(self.gerente_lista, AtualizarArqG, indent=4)


        with open(self.DirListaC, "w") as AtualizarArqC:
            json.dump(self.cliente_lista, AtualizarArqC, indent=4)



    def registrar_gerente(self, nome, endereco, telefone, senha,
    cpf):
        novo_gerente = Gerente(nome, endereco, telefone, senha,
    cpf)
        converterGerente = vars(novo_gerente)
        self.gerente_lista.append(converterGerente)
        self.atualizar_json()


    def registrar_cliente(self, nome, endereco, telefone, senha,
    cpf, saldo):
        novo_cliente = PessoaFisica(nome, endereco, telefone, senha, cpf, saldo)
        converterCliente = vars(novo_cliente)
        self.cliente_lista.append(converterCliente)
        self.atualizar_json()


    def registrar_empresa(self, nome, endereco, telefone, senha, cnpj, saldo):
        nova_empresa = PessoaJuridica(nome, endereco, telefone, senha, cnpj, saldo)
        converterEmpresa = vars(nova_empresa)
        self.cliente_lista.append(converterEmpresa)
        self.atualizar_json
