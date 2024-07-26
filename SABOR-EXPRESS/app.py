import os

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def finaliza_app():
    os.system('cls')
    print('Finalizando o app')

def exibir_opcoes():
    print('1 Cadastrar restaurante')
    print('2 Listar restaurantes')
    print('3 Ativar restaurante')
    print('4 Sair\n')

def escolher_opcao():
    opcao_esoclhida = int (input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_esoclhida}')

    if opcao_esoclhida == 1:
        print('Cadastrar restaurante')
    elif opcao_esoclhida == 2:
        print('Listar restaurantes')
    elif opcao_esoclhida == 3:    
        print('Ativar restaurante')
    elif opcao_esoclhida == 4:   
        finaliza_app()
    else:    
        print('Opção inválida!')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()