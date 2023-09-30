preço_original = float(input('Digite o valor do produto: R$'))
desconto = preço_original * (5/100)
desc = preço_original - desconto
print(f'O valor do produto é de R${preço_original:.2f}, com 5% de desconto é de R${desc:.2f}')
