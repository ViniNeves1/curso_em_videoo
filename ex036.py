#Inicio do programa

print('-=-'*30)
print('             Olá seja bem vindo ao assistente de emprestimos residenciais!               ')
print('-=-'*30)
print('             Para começarmos vamos precisar de algumas informações!                  ')
print('-=-'*30)


#Variaveis iniciais
casa = float(input('Qual o valor da residencia? R$'))
salario = float(input('Qual o valor do salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

#Calculos
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end="")
print(f' a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('PARABÉNS! Seu empréstimo foi aprovado!')
else:
    print('Infelizmente, seu emprestimo foi negado!')
