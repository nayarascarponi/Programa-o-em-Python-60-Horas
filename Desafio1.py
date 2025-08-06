# ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*


# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente.*

# *Regras Adicionais:
# **Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.***




print( 'HOTEL PYTHON - Reserva de Hospedagem ')
print( )


meu_carrinho = []
total_valores = []
diarias_totais = []
tipos_quartos = ['', 'Simples' , 'Duplo', 'Luxo']
valores = ['', 100.0, 150.0, 250.0 ]


cadastro1 = input('Digite o nome do hóspede 1:  ')
idade1= input('Digite a idade do hospede 1: ')


cadastro2 = input ('Digite o nome do hóspede 2: ')
idade2= input('Digite a idade do hospede 2: ')


cadastro3 = input ('Digite o nome do hóspede 3: ')
idade3= input('Digite a idade do hospede 3: ')




print(f'''Tipos de quarto:
      {tipos_quartos[1] } R$ {valores [1]}
      {tipos_quartos[2] } R$ {valores [2]}
      {tipos_quartos[3] } R$ {valores [3]}


''')

escolha1 = input(f'Escolha o quarto para o hóspede {cadastro1}:' )

if escolha1 == 'Simples':
    meu_carrinho.append(tipos_quartos[1])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [1]
    total_valores.append(diarias)
    
elif escolha1 == 'Duplo':
    meu_carrinho.append(tipos_quartos[2])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [2]
    total_valores.append(diarias)
elif escolha1 == 'Luxo':
    meu_carrinho.append(tipos_quartos[3])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [3]
    total_valores.append(diarias)





escolha2 = input(f'Escolha o quarto para o hóspede {cadastro2}: ')

if escolha2 == 'Simples':
    meu_carrinho.append(tipos_quartos[1])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [1]
    total_valores.append(diarias)
elif escolha2 == 'Duplo':
    meu_carrinho.append(tipos_quartos[2])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [2]
    total_valores.append(diarias)
elif escolha2 == 'Luxo':
    meu_carrinho.append(tipos_quartos[3])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [3]
    total_valores.append(diarias)






escolha3 = input(f'Escolha o quarto para o hóspede {cadastro3} : ')

if escolha3 == 'Simples':
    meu_carrinho.append(tipos_quartos[1])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [1]
    total_valores.append(diarias)
elif escolha3 == 'Duplo':
    meu_carrinho.append(tipos_quartos[2])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [2]
    total_valores.append(diarias)
elif escolha3 == 'Luxo':
    meu_carrinho.append(tipos_quartos[3])
    diarias = int(input('Escolha quantas diárias deseja reservar: ' ) )* valores [3]
    total_valores.append(diarias)

 




print(f'''Resumo do carrinho:
      Hospéde: {cadastro1} - Idade: {idade1} - Acomodação: {escolha1} - R$ {total_valores [0]}
      Hospéde: {cadastro2} - Idade: {idade2} - Acomodação: {escolha2} - R$ {total_valores [1]}
      Hospéde: {cadastro3} - Idade: {idade3} - Acomodação: {escolha3} - R$ {total_valores [2]}
           
      

''')

soma = sum(total_valores)

print('Total:R$', soma )

print(f'''Formas de pagamentos:' 
                      PIX - ID 1
                      Cartão de Crédito - ID 2
                      Boleto - ID 3
                  ''')

pagamento = input ('Digite a Forma de Pagamento: ' )
        
print('Pagamento realizado com sucesso !!!' )
