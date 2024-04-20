import os

def exibir_nome_do_programa():
    print(""" 
                                                        ╔═══╗──╔╗───────╔═══╗
                                                        ║╔═╗║──║║───────║╔══╝
                                                        ║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
                                                        ╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
                                                        ║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
                                                        ╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
                                                        ───────────────────────║║
                                                        ───────────────────────╚╝ """)

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair")

def finalizando_app():
    os.system("cls")                    # Limpa a tela do terminal antes de imprimir a mensagem "Encerrando" o programa"
    print("Encerrando Programa\n")

def escolher_opcao():
    opcao_escolhida = int(input("\nEscolha uma opçao: "))

    match opcao_escolhida:
        case 1:
            print("Cadastrar Restaurante")
        case 2:
            print("Listar Restaurantes")
        case 3:
            print("Ativar Restaurante")
        case 4:
            finalizando_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()