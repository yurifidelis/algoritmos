'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá 
pagar. Imprima os dados do programa com as mensagens adequadas.'''

peso = float(input("Digite o peso de peixes pescados (em quilos): "))

limite_peso = 50.0  # Limite estabelecido pelo regulamento (50 quilos)
excesso = 0.0
multa_por_quilo = 4.0
multa = 0.0

if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * multa_por_quilo

print("Peso de peixes:", peso, "kg")
if excesso > 0:
    print("Excesso de peso:", excesso, "kg")
    print("Valor da multa a ser pago: R$", multa)
else:
    print("Não há excesso de peso. Multa não aplicável.")

