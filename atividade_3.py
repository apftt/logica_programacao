#Enunciado: Você foi contratado para desenvolver um sistema de cobrança de banho para um petshop. Você ficou com a parte de desenvolver a interface com o funcionário.
#O petshop opera da seguinte maneira:
#    • Para cães com peso menor que 3 kg o valor base é de 40 reais;
#    • Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
#    • Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
#    • Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais; 

#    • Para cães com pelo curto (c) o multiplicador é 1;
#    • Para cães com pelo médio (m) o multiplicador é 1.5;
#    • Para cães com pelo longo (l) o multiplicador é 2;

#    • Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
#    • Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
#    • Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
#    • Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


#O valor final da conta é calculado da seguinte maneira:

#total = base * multiplicador + extra

# Mensagem boas-vindas
def msg(x):
    tam = len(x)
    if tam:
        print('+', '-' * tam, '+')
        print('|', x, '|')
        print('+', '-' * tam, '+')

# Definição do peso do cachorro
def cachorro_peso():
    print('-------------------- PESO DO CACHORRO --------------------')
    while True:
        try:
            base = float(input('Qual o peso do seu cachorro (Kg)? '))
            if (base < 3):
                return 40
            elif (base >= 3) and (base < 10):
                return 50
            elif (base >= 10) and (base < 30):
                return 60
            elif (base >= 30) and (base < 50):
                return 70
            else:
                print('Não aceitamos cachorros com peso superior a 50 kg.')
        except ValueError:
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
        multiplicador = multiplicador.upper()
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
    while True:
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
            return acumulador
        else:
            print('Opção inválida! Favor digitar uma opção existente.\n')


# Início do Main
msg('SEJA BEM-VINDO(A) AO PETSHOP DA ANA PAULA FERRONATTO')
print('\nA seguir escolha as opções desejadas para o melhor banho no seu cachorro\n')
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()
total = (base * multiplicador) + extra
print('O valor total do banho é de R$ {:.2f}'.format(total))

