# Questao 18
tamanhoMb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tempo = tamanhoMb / (velocidade * 8 / 60)

print(f"O tempo aproximado de download do arquivo é de {tempo:.2f} minutos.")
