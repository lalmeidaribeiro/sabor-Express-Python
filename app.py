import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Doces Dona Benta', 'categoria':'Doceria', 'ativo':False}
]

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa/Loja desenvolvido'''
    #print('𝓼𝓪𝓫𝓸𝓻 𝓮𝔁𝓹𝓻𝓮𝓼𝓼\n')
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exbiir_opcoes():
    '''Essa função exibe as opções do menu do lajo/programa desenvilvido'''
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurnates')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função tem como finalidade principal fechar o programa.'''
    exibir_subtitulo(print('Finalizando o App'))

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):  
    ''' Exibe um subtítulo estilizado na tela 
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*'* (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante 
    Inputs:
     - Nome restaurante;
     - Categoria.
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''#DocString 

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante  = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_restaurante}, foi cadastrado!!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Exibe os restaurantes presentes na lista
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurnate'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurnate in restaurantes:
        nome_restaurante = restaurnate['nome']
        categoria = restaurnate['categoria']
        ativo = 'Ativado' if restaurnate['ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o status do restaurante Ativado/Desativado
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrato = False
    
    for restaurnate in restaurantes:
        if nome_restaurante == restaurnate['nome']:
            restaurante_encontrato = True
            restaurnate['ativo'] = not restaurnate['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurnate['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrato:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def escolha_opcao(): 
    '''Exibi a solicitação de cada função que deve ser escolhida pelo usuário
    Outputs:
    -Executa a opção escolhida pelo usuário.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            print('Finalizar app')
        else:
             opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exbiir_opcoes()
    escolha_opcao()

if __name__ == '__main__':
    main()
