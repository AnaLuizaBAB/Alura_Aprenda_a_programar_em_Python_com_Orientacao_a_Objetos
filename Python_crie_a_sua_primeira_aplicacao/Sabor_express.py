import os

lista_de_restaurantes = [{'nome': 'Sushiloko', 'categoria': 'Japonesa', 'ativo': False},
                        {'nome': 'PizzaHut', 'categoria': 'Pizza', 'ativo': False},
                        {'nome': 'Buger King', 'categoria': 'Fast Food', 'ativo': True}]

def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa: Sabor Express'''

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
    '''Essa função exibe um menu de opções'''

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alterando Status do Restaurante")
    print("4. Sair")

def opcao_invalida():
    '''Essa função é responsável por exibir a mensagem: "Opção inválida. Tente novamente". E logo após realizar a volta ao menu principal. '''

    print("Opção inválida. Tente novamente.")
    input ("\nDigite uma tecla para voltar ao menu principal: ")
    main ()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir os subtítulos de cada uma das opções do menu principal'''

    os.system("cls")
    tamanho = (len(texto)) + 2
    print("*" * tamanho)
    print("*" + texto + "*")
    print("*" * tamanho)

    print()

def voltar_ao_menu_principal():
    '''Essa função é responsável por fazer o programa voltar ao menu principal'''

    input ("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def cadastrar_novo_restaurante():
    '''Função responsável pelo cadastro de novos restaurantes
    
    INPUTs:
    - Nome do restaurante
    - Categoria do restaurante

    OUTPUT:
    - Adiciona um restaurante a lista de restaurantes'''

    exibir_subtitulo(" Cadastro de novos restaurantes ")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_novos = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    lista_de_restaurantes.append(dados_novos)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Função responsável por listar os restaurantes cadastrados'''

    exibir_subtitulo(" Lista de restaurantes ")
    
    nome = 'Nome_do_Restaurante'
    categoria = 'Categoria'
    print(f'{nome.ljust(23)} | {categoria.ljust(20)} | Status')

    for restaurante in lista_de_restaurantes:
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f" - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}")

    voltar_ao_menu_principal()

def alterar_status_restaurante():
    '''Função responsável por alterar o status do restaurante de ativo para inativo ou vice versa
    
    INPUT:
    - Nome do restaurante

    OUTPUT:
    - Modifica o status do restaurante (de ativo para inativo ou vice versa)'''


    exibir_subtitulo(" Alterando Status do restaurante ")    

    nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")

    restaurante_encontrado = False

    for restaurante in lista_de_restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print (f"O status do restaurante foi ativado com sucesso." if restaurante['ativo'] else "O status do restaurante foi desativado com sucesso.")
    if not restaurante_encontrado:
        print("Restaurante não encontrado.")


    voltar_ao_menu_principal()

def finalizando_app():
    '''Função responsável por exibir uma mensagem de finalização do programa'''

    os.system("cls")                    # Limpa a tela do terminal antes de imprimir a mensagem "Encerrando" o programa"
    print("Encerrando Programa\n")

def escolher_opcao():
    '''Função responsável por fazer o usuário escolher uma das opções do menu principal
    
    INPUT:
    - A opção do menu desejada'''

    try:                                                        # com a inclusão desse try, caso o usuário digite algo que não seja um número inteiro o programa
        opcao_escolhida = int(input("\nEscolha uma opçao: "))   # exibirá a mensagem "Opção Inválida".

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_status_restaurante()
            case 4:
                finalizando_app()
            case _:
               opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Função principal que inicia o programa'''
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()