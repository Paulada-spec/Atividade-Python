# Questao 14
peso = float(input("Digite o peso de peixes (em quilos): "))

limite = 50

if peso > limite:
    excesso = peso - limite
    multaKg = 4.00
    multa = excesso * multaKg
else:
    excesso = 0
    multa = 0    

print(f"Peso informado: {peso:.2f} kg")
print(f"Limite de peso: {limite} kg")

if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("Não houve excesso de peso. Sem multa a pagar.")