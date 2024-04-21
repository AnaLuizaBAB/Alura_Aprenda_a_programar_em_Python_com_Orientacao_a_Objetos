import os

lista_de_restaurantes = ["SushiLoko", "Peixe na Rede"]

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

def opcao_invalida():
    print("Opção inválida. Tente novamente.")
    input ("\nDigite uma tecla para voltar ao menu principal: ")
    main ()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def voltar_ao_menu_principal():
    input ("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes.")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    lista_de_restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes.")
    lista_de_restaurantes.sort()
    
    for restaurante in lista_de_restaurantes:
        print(f".{restaurante}")

    voltar_ao_menu_principal()


def finalizando_app():
    os.system("cls")                    # Limpa a tela do terminal antes de imprimir a mensagem "Encerrando" o programa"
    print("Encerrando Programa\n")

def escolher_opcao():
    try:                                                        # com a inclusão desse try, caso o usuário digite algo que não seja um número inteiro o programa
        opcao_escolhida = int(input("\nEscolha uma opçao: "))   # exibirá a mensagem "Opção Inválida".

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar Restaurante")
            case 4:
                finalizando_app()
            case _:
               opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()