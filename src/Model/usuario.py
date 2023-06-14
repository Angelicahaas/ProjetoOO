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
