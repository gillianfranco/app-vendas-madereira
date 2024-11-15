def escolha_tipo():
    # Solicita a escolha do tipo de madeira e verifica se a escolha é válida
    while True:
        print('Digite o tipo de madeira desejado: ')
        print('PIN - Tora de Pinho')
        print('PER - Tora de Peroba')
        print('MOG - Tora de Mogno')
        print('IPE - Tora de Ipê')
        print('IMB - Tora de Imbuia')
        escolha = input('>> ')

        if escolha != 'PIN' and escolha != 'PER' and escolha != 'MOG' and escolha != 'IPE' and escolha != 'IMB':
            print('Escolha inválida. Tente novamente.\n')
            continue

        break

    # Retorna o preço da madeira escolhida
    if escolha == 'PIN':
        return 150.44
    elif escolha == 'PER':
        return 170.20
    elif escolha == 'MOG':
        return 190.90
    elif escolha == 'IPE':
        return 210.10
    elif escolha == 'IMB':
        return 220.70


def qtd_toras():
    while True:
        # Solicita a quantidade de toras de madeira e verifica se a quantidade é válida
        try:
            qtd = float(input('Digite a quantidade de toras(m\u00B3): '))
            if qtd < 0:
                print('Quantidade inválida! Digite um valor maior que 0.\n')
                continue
            elif qtd > 2000:
                print('Não aceitamos pedidos com essa quantidade de toras. Por favor, digite uma nova quantidade.\n')
                continue
            break
        except ValueError:
            print('Valor inválido! Tente novamente.\n')
    print()

    # Define o desconto de acordo com a quantidade de toras de madeira
    desconto = 0
    if (qtd >= 100) and (qtd < 500):
        desconto = 4 / 100
    elif (qtd >= 500) and (qtd < 1000):
        desconto = 9 / 100
    elif (qtd >= 1000) and (qtd <= 2000):
        desconto = 16 / 100

    return qtd, desconto

def transporte():
   while True:
       # Solicita a escolha do tipo de transporte e verifica se a escolha é válida
       print('Escolha o tipo de transporte: ')
       print('1 - Transporte Rodoviário - R$1000.00')
       print('2 - Transporte Ferroviário - R$2000.00')
       print('3 - Transporte Hidroviário - R$2500.00')
       tipo_transporte = int(input('>> '))
       if tipo_transporte < 1 or tipo_transporte > 3:
           print('Escolha inválida! Tente novamente.\n')
           continue
       break

   # Define o valor a ser pago pelo tipo de transporte, conforme a escolha do usuário
   valor = 0
   if tipo_transporte == 1:
       valor = 1000
   elif tipo_transporte == 2:
       valor = 2000
   elif tipo_transporte == 3:
       valor = 2500

   return valor

# Programa principal

tipo_madeira = escolha_tipo()
qtd_toras = qtd_toras()
valor_transporte = transporte()

total = ((tipo_madeira * qtd_toras[0]) * (1-qtd_toras[1])) + valor_transporte

print(f'\nValor total: R${total:.2f}')