from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica
from gerente import Gerente
import json



usuario1 = PessoaFisica("Harleny", "Santa", 34287736, "Leny123", 2354528593, 20, 10, 10)
converterUsuario1 = vars(usuario1)

usuario2 = PessoaJuridica("Bomel" "Gama", 89567834, "190903kjn", 76590980, 1000, 0000, 8909, 999)
converterUsuario2 = vars(usuario2)

usuario3 = PessoaFisica("João", "Mato", 9896763452, "4321", 233423, 20009, 377, 987)
converterUsuario3 = vars(usuario3)

usuario4 = PessoaFisica("Gabi", "CudoMUndo", 8765474839, "5678", 777483, 87665, 7748, 87666)
converterUsuario4 = vars(usuario4)

usuario5 = PessoaFisica("Milton", "Seila", 877655445, "9876", 348934, 787346, 34345, 9883)
converterUsuario5 = vars(usuario5)

usuario6 = Gerente("Angellica", "Maranhão", 4198760098, "soulinda", 72983976490)
converterUsuario6 = vars(usuario6)


usuarios = []
gerente = []
usuarios.append(converterUsuario1)
usuarios.append(converterUsuario2)
usuarios.append(converterUsuario3)
usuarios.append(converterUsuario4) 
usuarios.append(converterUsuario5)
gerente.append(converterUsuario6)


with open("BancodeDados//usuarios.json", "w") as arq_usuarios:
          json.dump(usuarios, arq_usuarios, indent=4)

print(usuarios)



with open("BancodeDados//usergerente.json", "w") as arq_gerente:
          json.dump(gerente, arq_gerente, indent=4)
          
print(gerente)
