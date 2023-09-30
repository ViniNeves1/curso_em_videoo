num = int(input('Digite um número inteiro: '))
print('Agora escolha para qual base deseja converter:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
opção = int(input('Selecione a opção: '))

if opção == 1:
    print(f'O número {num} convertido para binário é igual {bin(num)[2:]}')
elif opção == 2:
    print(f'O numéro {num} convertido para octal é igual {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!')

