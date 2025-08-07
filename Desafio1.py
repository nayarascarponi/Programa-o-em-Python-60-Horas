 ## ***ATIVIDADE 1***

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# c = 0
# while c <=1000:
#     print(c)
#     c = c +1

# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.


# n = 0
# nomes= []

# while n <=10:
    
#     nome= input('Digite um nome: ')
#     nomes.append (nome)
#     n = n +1


# ## ***ATIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for*** 
# # Sistema de notas de alunos

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média






nome = 'maria'
senha = '123'

chances = 3

nota1 = 0
nota2 = 0
nota3 = 0
media = 0

while chances > 0:
    dig_nome = input('Login: ')
    dig_senha = input('Senha: ')
    if dig_nome == nome and dig_senha == senha:
        print('Bem vindo')
        

        escolha = input('Deseja inserir nota? sim/não')
        while escolha == 'sim':
            nota1 = float(input ("Digite Nota 1: "))
            nota2 = float(input ('Digite Nota 2: '))
            nota3 = float(input ('Digite Nota 3: '))
            break
            
        escolha = input('Deseja Calcular a Média? sim/não' )
        while escolha == 'sim':
            media = (nota1 + nota2 + nota3 ) / 3
            break

                



        print (f'''
                   Nota 1: {nota1}
                   Nota 2: {nota2}
                   Nota 3: {nota3} 

                   Média: {media}
                                                       
                   ''')
        print ('Até Logo')
        input('Digite enter para sair')
        break

    else:
        print('Nome ou Senha Incorretos')
        chances = chances - 1
        
        

else:
    print('Conta Bloqueada !')