r1 = int(input('Digite o primeiro segmento: '))
r2 = int(input('Digite o segundo segmento: '))
r3 = int(input('Digite o terceiro segmento: '))

if r1 == r2 and r1 == r3:
    t = 'EQUILÁTERO'
elif r1 == r2 or r1 == r3 or r2 == r3:
    t = 'ISÓSCELES'
else:
    t = 'ESCALENO'

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Estes valores PODEM formar um triângulo {t}')
else:
    print('Estes valores NÃO PODEM formar um triângulo!')
