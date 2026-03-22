# Calculadora de energia

# Entrada de dados
# Nome do Aparelho
nome_aparelho = input("Digite o nome do aparelho: ")

# Potência do aparelho em watts (W)
potencia = float(input("Digite a potência do aparelho (W): "))

# Tempo de uso em horas
tempo = float(input("Digite o tempo de uso (horas): "))

# Valor da energia por kWh (reais)
valor_kwh = float(input("Digite o valor do kWh (R$): "))


# Conversão de watts para quilowatts (kW)
potencia_kw = potencia / 1000


# Cálculo do consumo
# Fórmula: potência (kW) * tempo (h)
consumo = potencia_kw * tempo


# Cálculo do custo
# consumo (kWh) * valor do kWh
custo = consumo * valor_kwh


# Saída de dados
print("\n--- Resultado ---")
print("Seu aparelho:", nome_aparelho)
print(f"Consome: {consumo:.2f} kWh")
print(f"Gasta: R$ {custo:.2f}")