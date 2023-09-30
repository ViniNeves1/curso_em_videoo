km = int(input('Quantos kilometros foram percorridos? '))
dia = int(input('Quantos dias foi alugado o veiculo? '))
kilometro = km * 0.15
dias = dia * 60
total = kilometro + dias
print(f'O valor a ser pago é de R${total:.2f}')
