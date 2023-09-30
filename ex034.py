salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    new = salario + (salario * 15 / 100)
else:
    new = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${new:.2f} agora.')