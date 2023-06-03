from Usuario import Usuario

class PessoaJuridica(Usuario):

    def __init__(self, nome: str, endereco: str, telefone: int, senha: str, cnpj: str, saldo: int, historico: int, pagamento: int ):
     super().__init__(nome, endereco, telefone, senha)
     self.__cnpj = cnpj
     self.__saldo = saldo
     self.__historico = historico
     self.__pagamento = pagamento


    def get_nome(self) -> str:
       return self.__nome
    
    def set_nome(self, nome: str):
       self.nome = nome

    def get_endereco(self) -> str:
       return self.__endereco
    
    def set_endereco(self, endereco: str):
       self.endereco = endereco

    def get_telefone(self) -> int:
       return self.__teledone
    
    def set_telefone(self, telefone: int):
       self.telefone = telefone

    def get_senha(self) -> int:
       return self.__senha
    
    def set_senha(self, senha: int):
       self.senha = senha

    def get_cnpj(self) -> str:
       return self.__cnpj
    
    def set_cpf(self, cnpj: str):
       self.cpf = cnpj

    def get_saldo(self) -> int:
       return self.__saldo
    
    def set_saldo(self, saldo: int):
       self.saldo = saldo

    def get_historico(self) -> int:
       return self.__historico
    
    def set_historico(self, historico: int):
       self.historico = historico

    def get_pagamento(self) -> int:
       return self.__pagamento
    
    def set_pagamento(self, pagamento: int):
       self.pagamento = pagamento