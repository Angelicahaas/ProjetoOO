from usuario import Usuario 

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
