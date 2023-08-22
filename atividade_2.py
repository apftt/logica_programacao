# Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
# A Sorveteria possui seguinte relação:

#  • 1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
#  • 2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
#  • 3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

print('Bem-vindo a Sorveteria da Ana Paula Ferronatto!')
print('-------------------------------------CARDÁPIO--------------------------------------')
print('| N° DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |       R$ 6,00          |       R$ 7,00      |        R$ 8,00      |')
print('|      2      |       R$11,00          |       R$13,00      |        R$15,00      |')
print('|      3      |       R$15,00          |       R$18,00      |        R$21,00      |')

acumulador = 0
while True:
    sabor = input('Favor digite o código do sabor desejado (tr/pr/es): ')
    sabor = sabor.lower() #para evitar transtorno se o cliente digitar com letra maiúscula
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Opção inválida. Favor corrigir o código de sabor solicitado!')
        continue #caso for digitado código errado voltará ao início

    bolas = input('Favor digite o número de bolas de sorvete desejado (1/2/3): ')
    if bolas != '1' and bolas != '2' and bolas != '3':
        print('Opção inválida. Favor corrigir o número de bolas de sorvete desejado!')
        continue #caso digitar n° de bolas inexistente voltará ao início

    if sabor == 'tr' and bolas == '1':
        print('Você escolheu 1 bola do sabor de sorvete Tradicional.')
        acumulador = acumulador + 6 #pega o valor contido no acumulador e soma 6
    elif sabor == 'tr' and bolas == '2':
        print('Você escolheu 2 bolas do sabor de sorvete Tradicional.')
        acumulador = acumulador + 11 #pega o valor contido no acumulador e soma 11
    elif sabor == 'tr' and bolas == '3':
        print('Você escolheu 3 bolas do sabor de sorvete Tradicional.')
        acumulador = acumulador + 15 #pega o valor contido no acumulador e soma 15

    elif sabor == 'pr' and bolas == '1':
        print('Você escolheu 1 bola do sabor de sorvete Premium.')
        acumulador = acumulador + 7 #pega o valor contido no acumulador e soma 7
    elif sabor == 'pr' and bolas == '2':
        print('Você escolheu 2 bolas do sabor de sorvete Premium.')
        acumulador = acumulador + 13 #pega o valor contido no acumulador e soma 13
    elif sabor == 'pr' and bolas == '3':
        print('Você escolheu 3 bolas do sabor de sorvete Premium.')
        acumulador = acumulador + 18 #pega o valor contido no acumulador e soma 18

    elif sabor == 'es' and bolas == '1':
        print('Você escolheu 1 bola do sabor de sorvete Especial.')
        acumulador = acumulador + 8 #pega o valor contido no acumulador e soma 8
    elif sabor == 'es' and bolas == '2':
        print('Você escolheu 2 bolas do sabor de sorvete Especial.')
        acumulador = acumulador + 15 #pega o valor contido no acumulador e soma 15
    elif sabor == 'es' and bolas == '3':
        print('Você escolheu 3 bolas do sabor de sorvete Especial.')
        acumulador = acumulador + 21 #pega o valor contido no acumulador e soma 21

    outro_ped = input('Deseja realizar mais algum pedido (S/N)? ')
    outro_ped = outro_ped.upper() #resolve-se o problema de digitar 's' ou 'n'
    if outro_ped == 'S':
        continue #realiza outro pedido
    else:
        print('O valor a ser pago é de R$ {:.2f}'.format(acumulador))
        print('\nObrigado pela preferência! Volte sempre...')
        break #realiza o encerramento do programa.