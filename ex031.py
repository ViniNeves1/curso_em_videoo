distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    print(f'Você está iniciando uma viagem de: {distancia:.1f} KM')
    valor = distancia * 0.50
    print(f'O valor da viagem é de: R${valor:.2f}')
else:
    print(f'Você está iniciando uma viagem de: {distancia:.1f} KM')
    valor = distancia * 0.45
    print(f'O valor da viagem é de: R${valor:.2f}')
print('TENHA UMA BOA VIAGEM!')