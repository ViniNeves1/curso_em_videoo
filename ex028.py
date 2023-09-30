import random
sorteado = random.randint(0,5)
num = int(input('Em que número eu pensei?: '))
if num == sorteado:
    print('Você venceu!')
else:
    print('Você errou! E eu venci!')
print(f'O número sorteado pelo computador foi: {sorteado}')