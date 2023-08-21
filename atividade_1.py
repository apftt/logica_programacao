# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de  vendas dessa empresa X é dar desconto maiores por unidade as informações abaixo:

#    • Se quantidade for menor que 200 o desconto será de 0%;
#    • Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
#    • Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
#    • Se quantidade for igual ou maior que 2000 o desconto será de 15%;


print('Sejam bem-vindos a loja Ana Paula Ferronatto')
print('PROMOÇÕES DE CAMISAS: LEVE MAIS, PAGUE MENOS!!!')
print('VALOR UNITÁRIO: 80 REAIS')

# Após boas-vindas inicia-se o processo de venda:

qtd = int(input('\nQuantas peças você deseja levar? '))
preco = 80

# Cálculo da quantidade de produto inferior a 200 peças:
if (qtd < 200):
    valor = qtd * preco
    print('O valor da compra é de {} reais.'.format(valor))

# Cálculo da quantidade de produtos entre 200 e 999 peças:
elif qtd >= 200 and qtd < 1000:
    valor = qtd * preco
# Aqui é calculada a quantidade vezes o preço com desconto de 5%:
    prom = qtd * preco * (1 - 0.05)
    print('O valor da compra SEM desconto é de {} reais. \nO valor COM desconto é de {} reais.'.format(valor, prom))

# Cálculo da quantidade de produtos entre 1000 e 1999 peças:
elif qtd >= 1000 and qtd < 2000:
    valor = qtd * preco
# Aqui é calculada a quantidade vezes o preço com desconto de 10%:
    prom = qtd * preco * (1 - 0.10)
    print('O valor da compra SEM desconto é de {} reais. \nO valor COM desconto é de {} reais.'.format(valor, prom))

# Cálculo da quantidade de produtos igual ou superior a 2000 peças:
elif qtd >= 2000:
    valor = qtd * preco
# Aqui é calculada a quantidade vezes o preço com desconto de 15%:
    prom = qtd * preco * (1 - 0.15)
    print('O valor da compra SEM desconto é de {} reais. \nO valor COM desconto é de {} reais.'.format(valor, prom))
else:
    print('Programa encerrado')

print('\nAgradecemos a preferência. Volte sempre!')