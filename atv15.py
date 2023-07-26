# Questao 15
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

ir_desconto = 0.11 * salario_bruto
inss_desconto = 0.08 * salario_bruto
sindicato_desconto = 0.05 * salario_bruto

salario_liquido = salario_bruto - (ir_desconto + inss_desconto + sindicato_desconto)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de Imposto de Renda (11%): R$ {ir_desconto:.2f}")
print(f"Desconto de INSS (8%): R$ {inss_desconto:.2f}")
print(f"Desconto de Sindicato (5%): R$ {sindicato_desconto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
