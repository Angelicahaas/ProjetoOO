class Usuario():

    def __init__(self, nome, endereco, telefone, senha):
        self.nome = nome
        self.endereco = endereco
        self.teledone = telefone
        self.senha = senha


    def get_nome(self) -> str:
       return self.nome
    
    def set_nome(self, nome: str):
       self.nome = nome

    def get_endereco(self) -> str:
       return self.endereco
    
    def set_endereco(self, endereco: str):
       self.endereco = endereco

    def get_telefone(self) -> int:
       return self.telefone
    
    def set_telefone(self, telefone: int):
       self.telefone = telefone

    def get_senha(self) -> int:
       return self.senha
    
    def set_senha(self, senha: int):
       self.senha = senha



class PessoaJuridica(Usuario):

    def __init__(self, nome, endereco, telefone, senha, cnpj, saldo, historico, pagamento):
     super().__init__(nome, endereco, telefone, senha)
     self.cnpj = cnpj
     self.saldo = saldo
     self.historico = historico
     self.pagamento = pagamento


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
       return self.cnpj
    
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


       
class PessoaFisica(Usuario):

    def __init__(self, nome, endereco, telefone, senha,
    cpf, saldo, historico, pagamento):
     super().__init__(nome, endereco, telefone, senha)
     self.cpf = cpf
     self.saldo = saldo
     self.historico = historico
     self.pagamento = pagamento
     

    def get_nome(self) -> str:
       return self.nome
    
    def set_nome(self, nome: str):
       self.nome = nome

    def get_endereco(self) -> str:
       return self.enderecondereco
    
    def set_endereco(self, endereco: str):
       self.endereco = endereco

    def get_telefone(self) -> int:
       return self.telefone
    
    def set_telefone(self, telefone: int):
       self.telefone = telefone

    def get_senha(self) -> int:
       return self.senha
    
    def set_senha(self, senha: int):
       self.senha = senha

    def get_cpf(self) -> str:
       return self.cpf
    
    def set_cpf(self, cpf: str):
       self.cpf = cpf

    def get_saldo(self) -> int:
       return self.saldo
    
    def set_saldo(self, saldo: int):
       self.saldo = saldo

    def get_historico(self) -> int:
       return self.historico
    
    def set_historico(self, historico: int):
       self.historico = historico

    def get_pagamento(self) -> int:
       return self.pagamento
    
    def set_pagamento(self, pagamento: int):
       self.pagamento = pagamento


class Gerente(Usuario):

    def __init__(self, nome, endereco, telefone, senha,
    cpf):
     super().__init__(nome, endereco, telefone, senha)
     self.cpf = cpf


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

    def get_cpf(self) -> str:
       return self.__cpf
    
    def set_cpf(self, cpf: str):
       self.cpf = cpf
 