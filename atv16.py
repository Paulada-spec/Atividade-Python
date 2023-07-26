# Questao 16
area = float(input("Qual o tamanho em metros quadrados da área a ser pintada:"))

litros = area / 3

numLatas = int(litros / 18)
if litros % 18 != 0:
    numLatas += 1

precoLata = 80.00
precoTotal = numLatas * precoLata

print("Quantidade de latas de tinta a serem compradas: ",numLatas)
print("Preço total: R$" ,precoTotal)