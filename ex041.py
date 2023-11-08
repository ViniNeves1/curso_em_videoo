import sys
from datetime import date
ano = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: JUNIOR.')
elif idade > 19 and idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: SÊNIOR.')
elif idade > 25:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: MASTER.')
