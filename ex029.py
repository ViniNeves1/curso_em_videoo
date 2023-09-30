vel=float(input('Qual a velocidade do carro?: '))
if vel > 80:
    print('Você foi multado!')
    velo = (vel - 80) * 7
    print('A VELOCIDADE MÁXIMA PERMITIDA É DE 80 KM/H')
    print(f'Você deve pagar uma multa de R${velo:.2f}!')
else:
    print('Você não foi multado! Boa Viagem!')
