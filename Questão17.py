import math

area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_tinta = area_pintada / 6  # Cálculo da quantidade de litros de tinta necessários

# Quantidade de latas de 18 litros
latas_18l = math.ceil(litros_tinta / 18)
preco_latas_18l = latas_18l * 80.0

# Quantidade de galões de 3,6 litros
galoes_3_6l = math.ceil(litros_tinta / 3.6)
preco_galoes_3_6l = galoes_3_6l * 25.0

# Quantidade de latas e galões misturados
latas_misturadas = math.ceil(litros_tinta / 18)
galoes_misturados = math.ceil((litros_tinta % 18) / 3.6)
preco_misturado = (latas_misturadas * 80.0) + (galoes_misturados * 25.0)

print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de tinta: ", latas_18l)
print("Preço total: R$", preco_latas_18l)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões de tinta: ", galoes_3_6l)
print("Preço total: R$", preco_galoes_3_6l)

print("\nSituação 3: Misturar latas e galões")
print("Quantidade de latas de tinta: ", latas_misturadas)
print("Quantidade de galões de tinta: ", galoes_misturados)
print("Preço total: R$", preco_misturado)
