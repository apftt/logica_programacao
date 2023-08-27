# Mensagem boas-vindas
def msg(x):
    tam = len(x) # para ficar borda do tamanho do texto digitado
    if tam:
        print('+', '-' * tam, '+')
        print('|', x, '|')
        print('+', '-' * tam, '+')

# Definição do peso do cachorro
def cachorro_peso():
    print('-------------------- PESO DO CACHORRO --------------------')
    while True: #garante que a função retorne uma opção válida
        try:
            peso = float(input('Qual o peso do seu cachorro (Kg)? ')) #caso seja digitado valor não inteiro
            if (peso < 3):
                return 40
            elif (peso >= 3) and (peso < 10):
                return 50
            elif (peso >= 10) and (peso < 30):
                return 60
            elif (peso >= 30) and (peso < 50):
                return 70
                break
            else:
                print('Não aceitamos cachorros com peso superior a 50 kg.')
        except ValueError: #caso seja digitado letra ou valor inválido
            print('Favor digitar peso válido.')

# Definição tamanho do pelo do animal
def cachorro_pelo():
    print('\n---------------TAMANHO DO PELO DO CACHORRO----------------')
    while True:
        multiplicador = input('Escolha a opção referente ao tamanho do pelo do seu cachorro (c/m/l): \n' +
                              'C - Pelo curto \n' +
                              'M - Pelo médio \n' +
                              'L - Pelo Longo \n' +
                              '>>  ')
        multiplicador = multiplicador.upper() #transforma as opções digitadas em letras maiúsculas
        # conforme a opção digitada abaixo retornará o multiplicador para cálculo
        if multiplicador == 'C':
            return 1
        elif multiplicador == 'M':
            return 1.5
        elif multiplicador == 'L':
            return 2
        else:
            print('Opção inválida! Favor digitar novamente.\n')


# Definição adicionais
def cachorro_extra():
    print('\n-----------------------ADICIONAIS-------------------------')
    acumulador = 0
    while True: #garante que a função retorne uma opção válida
        extra = input('Deseja algum serviço adicional? Favor digite o número do serviço desejado: \n' +
          '1 - Cortar unhas; \n' +
          '2 - Escovar os dentes; \n' +
          '3 - Limpar as orelhas; \n' +
          '0 - Não desejo nenhum serviço adicional. \n' +
          '>> ')
        if extra == '1':
            acumulador = acumulador + 10
            continue #volta para o início do loop
        elif extra == '2':
            acumulador = acumulador + 12
            continue #volta para o início do loop
        elif extra == '3':
            acumulador = acumulador + 15
            continue #volta para o início do loop
        elif extra == '0':
            return acumulador #Para não zerar se tiver algum adicional já selecionado
        else:
            print('Opção inválida! Favor digitar uma opção existente.\n')


# Início do Main
msg('SEJA BEM-VINDO(A) AO PETSHOP DA ANA PAULA FERRONATTO')
print('\nA seguir escolha as opções desejadas para o melhor banho no seu cachorro\n')
base = cachorro_peso() #Pega o valor da base referente ao valor do peso
multiplicador = cachorro_pelo() #pega o valor referente ao tamanho do pelo para multiplicação
extra = cachorro_extra() #adicionada o valor da quantidade de adicionais escolhidos
total = (base * multiplicador) + extra
print('O valor total do banho é de R$ {:.2f} (peso: {} * pelo: {} + adicional(is): {})'.format(total,base,multiplicador,extra)) #coloca :.2f dentro das chaves para valor ficar com apenas duas casas decimais


