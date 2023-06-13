from telalogin import TelaLogin
from telasenha import TelaSenha
import json

if __name__ == "__main__":

    dirUsers = "BancodeDados//usuarios.json"
    dirGerente = "BancodeDados/usergerente.json"


    with open(dirUsers) as arq_usuarios:
        usuarios = json.load(arq_usuarios)