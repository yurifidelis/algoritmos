import math

area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de litros de tinta necessários
litros_tinta = area_pintada / 3

# Cálculo da quantidade de latas de tinta necessárias
latas_tinta = math.ceil(litros_tinta / 18)

# Cálculo do preço total das latas de tinta
preco_lata = 80.0
preco_total = latas_tinta * preco_lata

print("Quantidade de latas de tinta necessárias:", latas_tinta)
print("Preço total das latas de tinta: R$", preco_total)
