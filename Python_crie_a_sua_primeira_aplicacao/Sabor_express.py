import os

print(""" 
                                                    ╔═══╗──╔╗───────╔═══╗
                                                    ║╔═╗║──║║───────║╔══╝
                                                    ║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
                                                    ╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
                                                    ║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
                                                    ╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
                                                    ───────────────────────║║
                                                    ───────────────────────╚╝ """)


def finalizando_app():
    os.system("cls")                    # Limpa a tela do terminal antes de imprimir a mensagem "Encerrando" o programa"
    print("Encerrando Programa\n")

print("1. Cadastrar Restaurante")
print("2. Listar Restaurantes")
print("3. Ativar Restaurante")
print("4. Sair")

opcao_escolhida = int(input("\nEscolha uma opçao: "))

if opcao_escolhida == 1:
    print("Cadastrar Restaurante")
if opcao_escolhida == 2:
    print("Listar Restaurantes")
if opcao_escolhida == 3:
    print("Ativar Restaurante")
if opcao_escolhida == 4:
    finalizando_app()