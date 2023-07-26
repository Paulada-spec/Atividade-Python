# Questao 17
import math

area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

litros_de_tinta_necessarios = area_a_ser_pintada / 6 * 1.1

quantidade_latas = math.ceil(litros_de_tinta_necessarios / 18)
quantidade_galoes = math.ceil(litros_de_tinta_necessarios / 3.6)

preco_lata = 80.00
preco_galao = 25.00

preco_total_latas = quantidade_latas * preco_lata
preco_total_galoes = quantidade_galoes * preco_galao

melhor_combinacao = min(
    ((latas, galoes) for latas in range(quantidade_latas + 1)
     for galoes in range(math.ceil((litros_de_tinta_necessarios - latas * 18) / 3.6) + 1)),
    key=lambda x: x[0] * preco_lata + x[1] * preco_galao
)

melhor_latas, melhor_galoes = melhor_combinacao
preco_total_misturado = melhor_latas * preco_lata + melhor_galoes * preco_galao

print(f"Quantidade de tinta a ser comprada:")
print(f"- Apenas latas de 18 litros: {quantidade_latas} latas")
print(f"- Apenas galões de 3,6 litros: {quantidade_galoes} galões")
print(f"- Melhor combinação (latas e galões): {melhor_latas} latas e {melhor_galoes} galões")
print(f"Preço total:")
print(f"- Apenas latas de 18 litros: R$ {preco_total_latas:.2f}")
print(f"- Apenas galões de 3,6 litros: R$ {preco_total_galoes:.2f}")
print(f"- Melhor combinação (latas e galões): R$ {preco_total_misturado:.2f}")
