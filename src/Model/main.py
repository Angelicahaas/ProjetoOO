from src.controller.cadastro import Cadastro, CadastroGerente

cadastro = Cadastro([])
cadastro_gerente = CadastroGerente("usergerente.json")

def exibir_menu():
    print("Bem-vindo ao Banco XYZ")
    print("1. Cadastrar novo cliente")
    print("2. Excluir cliente")
    print("3. Listar clientes")
    print("4. Cadastrar novo gerente")
    print("5. Excluir gerente")
    print("6. Listar gerentes")
    print("0. Sair")

def cadastrar_cliente():
    tipo_cliente = input("Digite o tipo de cliente (Física ou Jurídica): ")

    if tipo_cliente.lower() == "física":
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        senha = input("Digite a senha do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        saldo = float(input("Digite o saldo inicial do cliente: "))

        cadastro.adicionar_cliente_fisico(nome, endereco, telefone, senha, cpf, saldo)
        cadastro.salvar_dados_fisica()

    elif tipo_cliente.lower() == "jurídica":
        nome = input("Digite o nome da empresa: ")
        endereco = input("Digite o endereço da empresa: ")
        telefone = input("Digite o telefone da empresa: ")
        senha = input("Digite a senha da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ")
        saldo = float(input("Digite o saldo inicial da empresa: "))

        cadastro.adicionar_cliente_juridico(nome, endereco, telefone, senha, cnpj, saldo)
        cadastro.salvar_dados_juridicos()

    else:
        print("Tipo de cliente inválido!")

def excluir_cliente():
    cpf = input("Digite o CPF do cliente a ser excluído: ")
    cadastro.excluir_cliente_fisico(cpf)

def listar_clientes():
    cadastro.listar_cliente_fisico()

def cadastrar_gerente():
    nome = input("Digite o nome do gerente: ")
    senha = input("Digite a senha do gerente: ")
    matricula = input("Digite a matrícula do gerente: ")

    cadastro_gerente.adicionar_gerente(nome, senha, matricula)
    cadastro_gerente.salvar_dados_gerente()

def excluir_gerente():
    matricula = input("Digite a matrícula do gerente a ser excluído: ")
    cadastro_gerente.excluir_gerente(matricula)

def listar_gerentes():
    cadastro_gerente.listar_gerentes()

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        excluir_cliente()
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        cadastrar_gerente()
    elif opcao == "5":
        excluir_gerente()
    elif opcao == "6":
        listar_gerentes()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
