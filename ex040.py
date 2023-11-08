import time
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

média = (n1 + n2) / 2

if média >= 7.0:
    print(f'Sua média foi {média}, e você está:')
    time.sleep(1.5)
    print(f'\033[1:32mAprovado!!!!\033[0m')
elif média >= 5.0 and média == 6.9:
    print(f'Sua média foi {média}, e você está:')
    time.sleep(1.5)
    print('\033[1:10mde Recuperação!!!!\033[0m')
elif média < 5.0:
    print(f'Sua média foi {média}, e você está:')
    time.sleep(1.5)
    print('\033[1:31mReprovado!!!!\033[0m')
