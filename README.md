# app-vendas-madereira
**Descrição:** Projeto para praticar lógica de programação em Python, que coleta o pedido de toras de madeira, calcula o valor total e adiciona o custo do frete conforme o tipo de transporte escolhido.

## Try yourself!
**Proposta:** Você foi contratado para desenvolver um sistema de vendas para uma Empresa Y, que comercializa toras de árvores para outras empresas que vendem madeira. Sua responsabilidade é desenvolver a interface com o cliente.

A Empresa Y opera as vendas da seguinte maneira:
- Tora de Pinho (PIN): o valor do metro cúbico (m³) é de R$140,40.
- Tora de Peroba (PER): o valor do metro cúbico (m³) é de R$170,20.
- Tora de Mogno (MOG): o valor do metro cúbico (m³) é de R$190,90.
- Tora de Ipê (IPE): o valor do metro cúbico (m³) é de R$210,10.
- Tora de Imbuia (IMB): o valor do metro cúbico (m³) é de R$220,70.

Descontos por quantidade de toras (em m³):
- Menor que 100: não há desconto (0%).
- De 100 a 499: o desconto é de 4%.
- De 500 a 999: o desconto é de 9%.
- De 1000 a 2000: o desconto é de 16%.
- Acima de 2000: pedidos com essa quantidade de toras não são aceitos.

Adicional de transporte:
- Transporte rodoviário (1): valor extra de R$1000.
- Transporte ferroviário (2): valor extra de R$2000.
- Transporte hidroviário (3): valor extra de R$2500.

O valor final da conta é calculado da seguinte forma:

$$total = ((tipoMadeira * qtdToras) * (1 - desconto)) + transporte$$