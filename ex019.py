import random
n1 = str(input('Qual o primeiro aluno? '))
n2 = str(input('Qual o segundo aluno? '))
n3 = str(input('Qual o terceiro aluno? '))
n4 = str(input('Qual o quarto aluno? '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
