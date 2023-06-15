from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica
from gerente import Gerente
import json

class Cadastro:

    def __init__(self, clientes, usuarios):
        self.clientes = []
        self.usuarios = usuarios
        self.carregar_dados()



    def carregar_dados_fisicos(self):

        try:
            with open("BancodeDados//usuarios.json","r") as arq_cliente:
                dados = json.load(arq_cliente)

                for cliente in dados:
                    cliente_f_objeto = PessoaFisica(
                        cliente['nome'],
                        cliente['telefone'],
                        cliente['endereco'],
                        cliente['cpf'],
                        cliente['saldo']
                    )
                    cliente_f_objeto.saldo = PessoaFisica['saldo']
                    self.clientes.append(cliente_f_objeto)

                print(f"Dados dos clientes carregados do arquivo com sucesso!.")
            
        except FileNotFoundError:
                
                print(f"O arquivo não existe. Será criado umm novo arquivo.")

    
    def salvar_dados_fisica(self):
         dados_fisicos = []
         for cliente in self.clientes:
              dados_fisicos.append({
                   'nome': PessoaFisica.get_nome,
                   'endereco': PessoaFisica.get_endereco,
                   'telefone': PessoaFisica.get_telefone,
                   'senha': PessoaFisica.get_senha,
                   'cpf': PessoaFisica.get_cpf,
                   'saldo': PessoaFisica.get_saldo

              })

         with open("BancodeDados//usuarios.json", "w") as arq_cliente:
            json.dump(dados_fisicos, arq_cliente, indent=4)

         print(f"Dados salvos no arquivo com sucesso!")

    def adicionar_cliente_fisico(self, nome, endereco, telefone, senha, cpf, saldo):
         cliente_fisico = PessoaFisica(nome, endereco,telefone, senha, cpf, saldo)
         self.cliente.append(cliente_fisico)
         
         print(f"Cliente {nome} adicionado com sucesso!")


    def excluir_cliente_fisico(self, cpf):
         
         for cliente in self.clientes:
              if cliente == cliente.cpf:
                  if cliente.saldo == 0:                   
                     self.clientes.remove(cliente)
                     print("Cliente {cliente.nome} removido com sucesso.")
                     self.salvar_dados_fisica()
                
                  else:
                     print("O cliente não pode ser removido pois ainda possui saldo na conta.")
                    
                  return
              print(f"Cliente com CPF {cpf} não encontrado.")

    
    def listar_cliente_fisico(self):

        if len(self.clientes) == 0:
            print("Não há cliente registrados.")

        else:
            print("Cliente registrados.")

            for cliente in self.clientes:
                print(f"Nome: {PessoaFisica.get_nome}, Endereco: {PessoaFisica.get_endereco},Telefone: {PessoaFisica.get_telefone}, Senha: {PessoaFisica.get_senha}, e CPF: {PessoaFisica.get_cpf}")



    def carregar_dados_juridicos(self):
        try:
            
            with open("BancodeDados//usuarios.json", "r") as arq_cliente:
                dados = json.load(arq_cliente)

                for cliente in dados:
                    cliente_j_objeto = PessoaJuridica(
                        cliente['nome'],
                        cliente['endereco'],
                        cliente['telefone'],
                        cliente['cnpj']
                    )
                    cliente_j_objeto.saldo = PessoaJuridica['saldo']
                    self.clientes.append(cliente_j_objeto)
                print(f"Dados da Empresa carregados do arquivo com sucesso!.")
            
        except FileNotFoundError:
                
                print(f"O arquivo não existe. Será criado umm novo arquivo.")


    def salvar_dados_juridica(self):
         dados_juridico = []
         for cliente in self.clientes:
              dados_juridico.append({
                   'nome': PessoaJuridica.get_nome,
                   'endereco': PessoaJuridica.get_endereco,
                   'telefone': PessoaJuridica.get_telefone,
                   'senha': PessoaJuridica.get_senha,
                   'cnpj': PessoaJuridica.get_cnpj,
                   'saldo': PessoaJuridica.get_saldo

              })

    
         with open("BancodeDados//usuarios.json", "w") as arq_cliente:
              json.demp(dados_juridico, arq_cliente, indent=4)

         print(f"Dados salvos no arquivo com sucesso!")
    

    def adicionar_cliente_juridico(self, nome, endereco, telefone, senha, cnpj, saldo):
         cliente_juridico = PessoaJuridica(nome, endereco,telefone, senha, cnpj, saldo)
         self.cliente.append(cliente_juridico)
         
         print(f"Empresa {nome} adicionado com sucesso!")


    def excluir_cliente_juridico(self, cpf):
         
         for cliente in self.clientes:
              if cliente == cliente.cpf:
                  if cliente.saldo == 0:                   
                     self.clientes.remove(cliente)
                     print("Empresa {cliente.nome} removido com sucesso.")
                     self.salvar_dados_fisica()
                
                  else:
                     print("O cliente não pode ser removido pois ainda possui saldo na conta.")
                    
                  return
              print(f"Cliente com CPF {cpf} não encontrado.")


    def adicionar_cliente_juridico(self, nome, endereco, telefone, senha, cnpj, saldo):
        cliente_juridico = PessoaJuridica(nome, endereco, telefone, senha, cnpj, saldo)
        self.cliente.append(cliente_juridico)

        print(print(f"Nome: {PessoaJuridica.get_nome}, Endereco: {PessoaJuridica.get_endereco},Telefone: {PessoaJuridica.get_telefone}, Senha: {PessoaJuridica.get_senha}, e CPF: {PessoaJuridica.get_cnpj}"))


class CadastroGerente:

    def __init__(self,usergerente):
        self.gerentes = []
        self.usergerente = usergerente
        self.carregar_dados()


    def carregar_dados_gerente(self):
        try:
            with open("BancodeDados//usergerente.json", "r") as arq_gerente:
                self.gerentes = json.load(arq_gerente)
            
            print(f"Dados dos gerentes carregados do arquivo {self.usergerente} com sucesso!")

        except FileNotFoundError:
            print(f"O arquivo {self.usergerente} não existe.")


    def salvar_dados_gerente(self):

        with open("BancodeDados//usergerente.json", "w") as arq_gerente:
            json.dump(self.gerentes, arq_gerente, indent=4)

        print(f"Dados do gerente salvos no arquivo {self.usergerente} com sucesso!")


