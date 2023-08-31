#Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerencialme de pessoas. Este software deve ter o seguinte menu e opções:

#    1) Cadastrar Colaborador
#    2) Consultar Colaborador
#        1. Consultar Todos 
#        2. Consultar por Id;
#        3. Consultar por Setor;
#        4. Retornar ao menu;
#    3) Remover Colaborador
#    4) Encerrar Programa

# Variáveis Globais
lista_colaboradores = []
id_global = 0

def cadastrar_colaborador(id):
    print('----------------------CADASTRAMENTO COLABORADOR---------------------------------')
    nome = input('\nDigite o nome do colaborador: ')
    setor = input('Digite o setor em que o colaborador trabalha: ')
    pagamento = float(input('Digite o valor do salário pago ao colaborador: '))
    #id += id_global + 1
    colaborador = { 'id': id,
                    'nome': nome,
                    'setor': setor,
                    'pagamento': pagamento}
    lista_colaboradores.append(colaborador)
    print('\n..: Colaborador cadastrado com sucesso! :.. \n')

    return id_global + 1


def consultar_colaborador():
    print('----------------------CONSULTA COLABORADOR(ES)---------------------------------')
    while True:
        opcao_consulta = input('\nDigite a opção desejada:\n'+
                      '1.Consultar Todos \n'+
                      '2.Consultar por ID\n'+
                      '3.Consulta por setor\n'+
                      '4.Retornar ao menu principal')

        opcao_consulta = int(opcao_consulta)

        if opcao_consulta == 1:
            if len(lista_colaboradores) == 0:
                print('\nNão existem colaboradores cadastrados!')
            else:
                for colaborador in lista_colaboradores:
                    print('ID: ', colaborador['id'], '- Nome:', colaborador['nome'], '- Setor:', colaborador['setor'], '- Pagamento: R$ ', colaborador['pagamento'])
        elif opcao_consulta == 2:
            id_pesquisar = int(input('Digite o ID do colaborador a ser consultado: '))
            achou = False
            for colaborador in lista_colaboradores:
                if colaborador['id'] == id_pesquisar:
                    print('ID: ', colaborador['id'], '- Nome:', colaborador['nome'], '- Setor:', colaborador['setor'], '- Pagamento: R$ ', colaborador['pagamento'])
                    achou = True
                    break
            if not achou:
                print('Colaborador não encontrado.')
        elif opcao_consulta == 3:
            setor_consulta = input('Digite o setor a ser consultado: ')
            encontrados = []
            for colaborador in lista_colaboradores:
                if colaborador['setor'] == setor_consulta:
                    encontrados.append(colaborador)

            if encontrados:
                for colaborador in encontrados:
                    print('ID: ', colaborador['id'], '- Nome:', colaborador['nome'], '- Setor:', colaborador['setor'], '- Pagamento: R$ ', colaborador['pagamento'])
            else:
                print('Colaborador não encontrado neste setor.')
        elif opcao_consulta == 4:
            return opcao_consulta
        else:
            print('Opção inválida')
def remover_colaborador():
    print('----------------------REMOÇÃO DE COLABORADORES---------------------------------')
    id_excluir = int(input('Digite o ID do colaborador a ser removido: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_excluir:
            lista_colaboradores.remove(colaborador)
            print('Colaborador ', colaborador['nome'], ' removido com sucesso!')
            return
    else:
        print("Colaborador não encontrado.")


#Início do Main
print('"SEJAM BEM-VINDOS AO SOFTWARE DE GERENCIAMENTO DE PESSOAS DA EMPRESA ANA PAULA FERRONATTO"\n')
print('--------------------------MENU PRINCIPAL--------------------------------')
while True:
    print("\nMenu:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    opcao_menu = int(input("\nEscolha uma opção: "))

    if opcao_menu == 1:
        id_global = cadastrar_colaborador(id_global)
    elif opcao_menu == 2:
        consultar_colaborador()
    elif opcao_menu == 3:
        remover_colaborador()
    elif opcao_menu == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")



