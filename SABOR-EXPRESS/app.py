import os

restaurantes = ['Pizza', 'Cebola']

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1 Cadastrar restaurante')
    print('2 Listar restaurantes')
    print('3 Ativar restaurante')
    print('4 Sair\n')

def finaliza_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para retornar ao menu!')  
    main()  

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()    

def cadastrar_novo_retaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def lista_restaurantes():
    exibir_subtitulo('Lista de restaurantes\n')    
    
    for restaurante in restaurantes:
        print(f'- {restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_esoclhida = int (input('Escolha uma opção: '))
        # print(f'Você escolheu a opção {opcao_esoclhida}')

        if opcao_esoclhida == 1:
            cadastrar_novo_retaurante()
        elif opcao_esoclhida == 2:
            lista_restaurantes()
        elif opcao_esoclhida == 3:    
            print('Ativar restaurante')
        elif opcao_esoclhida == 4:   
            finaliza_app()
        else:    
            opcao_invalida()
    except:    
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
    

if __name__ == '__main__':
    main()