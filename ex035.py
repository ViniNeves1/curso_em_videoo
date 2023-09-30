print('-='*20)
print('     Analisador de triângulos        ')
print('-='*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('DIgite o segundo segmento: '))
r3 = float(input('DIgite o terceiro segmento: '))
if r1 < r2 + r3:
    t = r2 + r3
if r2 < r1 + r3:
    t = r1 + r3
if r3 < r1 + r2:
    t = r1 + r2
    print(f'Esses valores formam um triângulo, \033[31mPARABÉNS!')
else:
    print('Esses valores não formam um triângulo')
