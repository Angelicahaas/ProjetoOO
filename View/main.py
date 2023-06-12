from telalogin import Login

tela_login = TelaLogin()
tela_login.mostrar()

if tela_login.validar():
    print("Login bem-sucedido!")
else:
    print("Crenciais inválidas.Tente novamente.")