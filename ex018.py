import math
a = int(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
print(f'O ângulo de {a:.1f} tem o SENO de {sen:.2f}')
cos = math.cos(math.radians(a))
print(f'O ângulo de {a:.1f} tem o COSSENO de {cos:.2f}')
tan = math.tan(math.radians(a))
print(f'O ângulo de {a:.1f} tem a TANGENTE de {tan:.2f}')
