frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A Letra A aparece {frase.count("a")} vezes na frase')
print(f'A primeria letra A apareceu na posição {frase.find("A")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
