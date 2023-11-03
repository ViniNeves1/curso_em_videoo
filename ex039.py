import sys
import time
from datetime import date
print('\033[1:36m-=-'*20)
print('   Seja bem vindo ao SERVIÇO DE ALISTAMENTO MILITAR!!!!!')
print('-=-'*20)
time.sleep(1.5)
print('     \033[1:91mQual o seu gênero?\033[0m ')
print('         \033[1:34mMasculino')
print('         \033[1:35mFeminino\033[0m')
selecione = str(input('     \033[1:32mSelecione a opção:\033[0m '))
time.sleep(1.5)
if selecione == 'Feminino' and 'feminino' and 'FEMININO':
    print('\033[1:36mEstamos analisando sua resposta, aguarde um momento!')
    time.sleep(1.5)
    print('\033[1:31mVocê não tem esta obrigação!')
    sys.exit()
else:
    print('\033[1:34m-=-'*20)
    print('         Vamos prosseguir com a analise!')
    print('-=-' * 20)
print('     \033[1:33mVocê já se alistou? ')
print('             \033[1:32mSim')
print('             \033[1:31mNão\033[0m')
selecione = str(input('     \033[1:32mSelecione a opção:\033[0m '))
print('\033[1:36mEstamos analisando sua resposta, aguarde um momento!')
time.sleep(1.5)
atual = date.today().year
nascimento = int(input('\033[1:33mQual o ano de nascimento? '))
print('\033[1:36mOK, Aguarde alguns instantes!')
time.sleep(1.5)
idade = atual - nascimento
print('\033[1:36mEstamos analisando sua resposta, aguarde um momento!')
time.sleep(1.5)
print(f'\033[1:94mQuem nasceu em \033[1:32m{nascimento}\033[0m, \033[1:94mtem \033[1:32m{idade}\033[0m '
      f'\033[1:94manos em \033[1:32m{atual}\033[0m')
if selecione == 'sim' and 'Sim' and 'SIM' and idade >= 18:
    ano = nascimento + 18
    print(f'\033[1:94mVocê se alistou em \033[1:32m{ano}\033[0m')
elif idade < 18:
    print(f'\033[1:94mVocê tendo \033[1:32m{idade}\033[0m \033[1:94manos. \nVocê ainda deverá se alistar!')
    saldo = 18 - idade
    print(f'\033[1:94mAinda falta \033[1:32m{saldo}\033[0m \033[1:94mano(s) para você se alistar!')
    ano = atual + saldo
    print(f'\033[1:94mVocê deverá se alistar em \033[1:32m{ano}\033[0m')
elif idade == 18:
    print(f'\033[1:94mVocê tendo \033[1:32m{idade}\033[0m \033[1:94manos. \nVocê deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'\033[1:94mVocê tem \033[1:32m{idade}\033[0m \033[1:94manos')
    saldo = idade - 18
    print(f'\033[1:94mVocê deveria ter se alistado a \033[1:32m{saldo}\033[0m \033[1:94mano(s)')
    ano = atual - saldo
